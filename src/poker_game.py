#!/usr/bin/env python3.11
"""
TODO:
- Add betting, calling, raising, folding
- Add 7 card stud
- Add 7 card draw
- Add Texas Hold 'em
"""

import random
from collections import Counter
import os


class Card:
    """
    Represents a standard playing card with a value and suit.

    Attributes:
        _rank (Rank): The card's value (2-10, Jack, Queen, King, Ace)
        _suit_value (Suit): The card's suit (Clubs, Diamonds, Hearts, Spades)
    """

    RANK_DICT = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "j": 11,
        "q": 12,
        "k": 13,
        "a": 14,
    }

    SUIT_SET = {"c", "d", "h", "s"}

    # Unicode symbols for suits
    SUIT_SYMBOLS = {
        "c": "♣",  # ♣
        "d": "♦",  # ♦
        "h": "♥",  # ♥
        "s": "♠",  # ♠
    }

    def __init__(self, rank: str, suit: str):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self) -> int:
        return self.RANK_DICT[self._rank]

    @property
    def suit(self) -> str:
        return self._suit

    def __lt__(self, other: "Card") -> bool:
        return self.RANK_DICT[self._rank] < other.RANK_DICT[other._rank]

    def __str__(self) -> str:
        # Use uppercase for face cards and Ace
        rank_display = self._rank.upper() if self._rank in {"j", "q", "k", "a"} else self._rank
        suit_symbol = self.SUIT_SYMBOLS[self._suit]
        return f"{rank_display}{suit_symbol}"


class Hand:
    """
    Abstract base class for card hands.

    Defines the basic interface that all hand types must implement, including
    hand comparison operations.

    Attributes:
        _cards (list[Card]): List of cards in the hand
        _hand_value: The calculated value of the hand (implementation specific)
    """

    def __init__(self, cards: list[Card]) -> None:
        self._cards = cards
        self._hand_value = None

    @property
    def get_hand(self) -> list:
        raise NotImplementedError()

    def __lt__(self, other):
        raise NotImplementedError()


class PokerHand(Hand):
    """
    Represents a poker hand of 5 cards.

    Implements poker hand ranking and comparison logic according to standard poker rules.
    Supports all standard poker hands from high card to royal flush.

    Attributes:
        _cards (list[Card]): List of 5 cards in the poker hand
        _hand_value: Tuple containing hand type and relevant card values for comparison
    """

    # Class constants
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __init__(self, cards: list[Card]) -> None:
        self._cards = cards
        self._hand_value = self.best_hand()

    # Returns a list where first element is an integer 1-14 representing a hand
    # (e.g. 10 = Royal Flush)
    # The remaining elements are the Card objects in the hand.
    @property
    def get_hand(self) -> list:
        cards = []
        cards.append(self._hand_value[0])
        for card in self._cards:
            cards.append(str(card))
        return cards

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, rank: int, suit: str) -> bool:
        for card in self._cards:
            if card.rank == rank and card.suit == suit:
                self._cards.remove(card)
                return True
        return False

    def update_best_hand(self):
        self._hand_value = self.best_hand()

    def __eq__(self, other: object) -> bool:
        # Determine if the two hands are equal in order of hands.
        if not isinstance(other, PokerHand):
            return NotImplemented
        if self._hand_value[0] == other._hand_value[0]:
            match self._hand_value[0]:
                # If both hands are Royal Flush, they are equal.
                case self.ROYAL_FLUSH:
                    return True
                # If both hands are Straight Flush, compare the highest card.
                case self.STRAIGHT_FLUSH:
                    return self._hand_value[1] == other._hand_value[1]
                # If both hands are Four of a Kind, compare the four of a kind value.
                case self.FOUR_OF_A_KIND:
                    return self._hand_value[1] == other._hand_value[1]
                # If both hands are Full House, compare the three of a kind value, then pair value.
                case self.FULL_HOUSE:
                    return self._hand_value[1] == other._hand_value[1] and self._hand_value[2] == other._hand_value[2]
                # If both hands are Flush, compare the highest card values.
                case self.FLUSH:
                    for i in range(1, 6):
                        if self._hand_value[i] != other._hand_value[i]:  # type: ignore
                            return False
                    # If all the card values are equal:
                    return True
                # If both hands are Straight, compare the highest card value.
                case self.STRAIGHT:
                    return self._hand_value[1] == other._hand_value[1]
                # If both hands are Three of a Kind, compare the three of a kind value
                # and the remaining card values.
                case self.THREE_OF_A_KIND:
                    for i in range(1, 4):
                        if self._hand_value[i] != other._hand_value[i]:  # type: ignore
                            return False
                    return True
                # If both hands are Two Pair, compare the higher value pair,
                # the lower value pair, and the remaining card.
                case self.TWO_PAIR:
                    return (
                        self._hand_value[1] == other._hand_value[1]
                        and self._hand_value[2] == other._hand_value[2]
                        and self._hand_value[3] == other._hand_value[3]
                    )
                # If both hands are One Pair, compare the pair value and remaining cards.
                case self.ONE_PAIR:
                    for i in range(1, 5):
                        if self._hand_value[i] != other._hand_value[i]:  # type: ignore
                            return False
                    return True
                # If both hands are High Card, compare all card values.
                case self.HIGH_CARD:
                    for i in range(1, 6):
                        if self._hand_value[i] != other._hand_value[i]:
                            return False
                    return True
                # If hand type is not recognized, raise an error.
                case _:
                    raise ValueError("Invalid hand value comparison - unexpected hand type")
        else:
            return False

    # Compare tuple returned by this Pokerhand's _hand_value to another Pokerhand.
    def __lt__(self, other: "PokerHand") -> bool:
        # Determine if the two hands are equal in order of hands.
        if not isinstance(other, PokerHand):
            return NotImplemented
        if self._hand_value[0] == other._hand_value[0]:
            match self._hand_value[0]:
                # If both hands are Royal Flush, they are equal.
                case self.ROYAL_FLUSH:
                    return False
                # If both hands are Straight Flush, compare the highest card.
                case self.STRAIGHT_FLUSH:
                    return self._hand_value[1] < other._hand_value[1]
                # If both hands are Four of a Kind, compare the four of a kind value.
                case self.FOUR_OF_A_KIND:
                    return self._hand_value[1] < other._hand_value[1]
                # If both hands are Full House, compare the three of a kind value first,
                # then the pair value.
                case self.FULL_HOUSE:
                    for i in range(1, 3):
                        if self._hand_value[i] < other._hand_value[i]:  # type: ignore
                            return True
                        if self._hand_value[i] > other._hand_value[i]:  # type: ignore
                            return False
                    # If both hands are equal
                    return False
                # If both hands are Flush, compare the highest card values in descending order.
                case self.FLUSH:
                    for i in range(1, 6):
                        if self._hand_value[i] < other._hand_value[i]:  # type: ignore
                            return True
                        if self._hand_value[i] > other._hand_value[i]:  # type: ignore
                            return False
                    # If both hands are equal
                    return False
                # If both hands are Straight, compare the highest card value.
                case self.STRAIGHT:
                    return self._hand_value[1] < other._hand_value[1]
                # If both hands are Three of a Kind, compare the three of a kind value first,
                # then the remaining card values in descending order.
                case self.THREE_OF_A_KIND:
                    for i in range(1, 4):
                        if self._hand_value[i] < other._hand_value[i]:  # type: ignore
                            return True
                        elif self._hand_value[i] > other._hand_value[i]:  # type: ignore
                            return False
                    # If both hands are equal
                    return False
                # If both hands are Two Pair, compare the higher value pair first,
                # then the lower value pair, and finally the remaining card.
                case self.TWO_PAIR:
                    for i in range(1, 4):
                        if self._hand_value[i] < other._hand_value[i]:  # type: ignore
                            return True
                        elif self._hand_value[i] > other._hand_value[i]:  # type: ignore
                            return False
                    # If both hands are equal
                    return False
                # If both hands are One Pair, compare the pair value first,
                # then the remaining card values in descending order.
                case self.ONE_PAIR:
                    for i in range(1, 5):
                        if self._hand_value[i] < other._hand_value[i]:  # type: ignore
                            return True
                        elif self._hand_value[i] > other._hand_value[i]:  # type: ignore
                            return False
                    # If both hands are equal
                    return False
                # If both hands are High Card, compare all cards values in decending order.
                case self.HIGH_CARD:
                    for i in range(1, 6):
                        if self._hand_value[i] < other._hand_value[i]:  # type: ignore
                            return True
                        elif self._hand_value[i] > other._hand_value[i]:  # type: ignore
                            return False
                    # If both hands are equal
                    return False
                # If hand type is not recognized, raise an error.
                case _:
                    raise ValueError("Invalid hand value comparison - unexpected hand type")
        else:
            return self._hand_value[0] < other._hand_value[0]

    def best_hand(self) -> tuple[int, int, int, int, int, int]:  # type:ignore
        def check_high_card():
            return max(value_list)

        def check_one_pair() -> bool:
            pair_count = 0
            for val in values_to_counts.values():
                if val == 2:
                    pair_count += 1
            return pair_count == 1

        def check_two_pair() -> bool:
            pair_count = 0
            for val in values_to_counts.values():
                if val == 2:
                    pair_count += 1
            return pair_count == 2

        def check_three_kind() -> bool:
            for val in values_to_counts.values():
                if val == 3:
                    return True
            return False

        def check_straight() -> bool:
            for i in range(len(value_list) - 1):
                if value_list[i] - value_list[i + 1] != 1:
                    return False
            return True

        def check_flush() -> bool:
            return len(suit_set) == 1

        def check_full_house() -> bool:
            return one_pair and three_kind

        def check_four_kind() -> bool:
            for val in values_to_counts.values():
                if val == 4:
                    return True
            return False

        def check_straight_flush() -> bool:
            return flush and straight

        def check_royal_flush() -> bool:
            return straight_flush and high_card == Card.RANK_DICT["a"]

        # A -1 in indexes 1-5 of the return tuple indicates value not used.
        # Royal Flush does not need any index 1-5.
        # Four of a Kind places its value at index 1, and the fifth card at index 2.
        # Straigt Flush, Straight, and High Card place High Card at index 1.
        # Full House places its Three of a Kind value at index 1, and the pair value at index 2.
        # Flush places all five card values in descending order in indexes 1-5.
        # Three of a Kind places its value at index 1, and the remaining card values in descending
        # at index 2 and 3.
        # Two Pair places its higher value at index 1, and second value at index 2.
        # Pair places its value at index 1, and the other three value in descending order at
        # indexes 2-4.
        # and the remaining card in the third int value.
        def result_tuple(
            hand: int,
        ) -> tuple[int, int, int, int, int, int]:  # type:ignore
            match hand:
                case self.ROYAL_FLUSH:
                    return (self.ROYAL_FLUSH, -1, -1, -1, -1, -1)
                case self.STRAIGHT_FLUSH:
                    return (self.STRAIGHT_FLUSH, high_card, -1, -1, -1, -1)
                case self.FOUR_OF_A_KIND:
                    for val, cnt in values_to_counts.items():
                        if cnt == 4:
                            fok = val
                    return (self.FOUR_OF_A_KIND, fok, -1, -1, -1, -1)  # type: ignore
                case self.FULL_HOUSE:
                    pair = 0
                    tok = 0
                    for val, cnt in values_to_counts.items():
                        if cnt == 2:
                            pair = val
                        if cnt == 3:
                            tok = val
                    return (self.FULL_HOUSE, tok, pair, -1, -1, -1)
                case self.FLUSH:
                    a = value_list[0]
                    b = value_list[1]
                    c = value_list[2]
                    d = value_list[3]
                    e = value_list[4]
                    return (self.FLUSH, a, b, c, d, e)
                case self.STRAIGHT:
                    return (self.STRAIGHT, high_card, -1, -1, -1, -1)
                case self.THREE_OF_A_KIND:
                    other_cards = []
                    for val, cnt in values_to_counts.items():
                        if cnt == 3:
                            tok = val
                        if cnt == 1:
                            other_cards.append(val)
                    higher = max(other_cards)
                    lower = min(other_cards)
                    return (self.THREE_OF_A_KIND, tok, higher, lower, -1, -1)  # type: ignore
                case self.TWO_PAIR:
                    pairs = []
                    for val, cnt in values_to_counts.items():
                        if cnt == 2:
                            pairs.append(val)
                        if cnt == 1:
                            remaining = val
                    higher = max(pairs)
                    lower = min(pairs)
                    return (self.TWO_PAIR, higher, lower, remaining, -1, -1)  # type: ignore
                case self.ONE_PAIR:
                    for val, cnt in values_to_counts.items():
                        if cnt == 2:
                            pair = val
                    b = value_list[2]
                    c = value_list[3]
                    d = value_list[4]
                    return (self.ONE_PAIR, pair, b, c, d, -1)  # type: ignore
                case self.HIGH_CARD:
                    a = value_list[0]
                    b = value_list[1]
                    c = value_list[2]
                    d = value_list[3]
                    e = value_list[4]
                    return (self.HIGH_CARD, a, b, c, d, e)

        suit_set = {card.suit for card in self._cards}
        value_list = [card.rank for card in self._cards]
        value_list.sort(reverse=True)
        values_to_counts = Counter(value_list)

        high_card = check_high_card()  # High card holds actual card value.
        one_pair = check_one_pair()
        two_pair = check_two_pair()
        three_kind = check_three_kind()
        flush = check_flush()
        straight = check_straight()
        full_house = check_full_house()
        four_kind = check_four_kind()
        straight_flush = check_straight_flush()
        royal_flush = check_royal_flush()

        hands = [
            (royal_flush, self.ROYAL_FLUSH),
            (straight_flush, self.STRAIGHT_FLUSH),
            (four_kind, self.FOUR_OF_A_KIND),
            (full_house, self.FULL_HOUSE),
            (flush, self.FLUSH),
            (straight, self.STRAIGHT),
            (three_kind, self.THREE_OF_A_KIND),
            (two_pair, self.TWO_PAIR),
            (one_pair, self.ONE_PAIR),
            (True, self.HIGH_CARD),  # Always true as fallback
        ]

        # The first is_hand that is True is the highest hand.
        for is_hand, hand in hands:
            if is_hand:
                return result_tuple(hand)


class Deck:
    """
    Represents a standard 52-card playing deck.

    Manages deck state including dealt cards and provides methods for dealing
    cards randomly.

    Attributes:
        _deck (dict[int, Card]): Maps card IDs to Card objects
        _dealt (list[int]): List of IDs of cards that have been dealt
    """

    def __init__(self) -> None:
        self._deck: dict[int, Card] = {}
        self._dealt: list[int] = []
        self._build_deck()

    def _build_deck(self) -> None:
        count = 1
        for suit in Card.SUIT_SET:
            for rank in Card.RANK_DICT:
                new_card = Card(rank, suit)
                self._deck[count] = new_card
                count += 1

    def random_deal(self, hand_size: int) -> list[Card]:
        hand = []
        # Convert range to set and remove dealt cards via set subtraction.
        available_cards = set(range(1, len(self._deck) + 1)) - set(self._dealt)
        # Convert back to list for random.sample.
        sample = random.sample(list(available_cards), hand_size)

        for card_num in sample:
            hand.append(self._deck[card_num])
            self._dealt.append(card_num)

        return hand

    def random_deal_one(self) -> Card:
        # Convert range to set and remove dealt cards via set subtraction.
        available_cards = set(range(1, len(self._deck) + 1)) - set(self._dealt)
        # Convert back to list for random.sample.
        sample = random.sample(list(available_cards), 1)
        # random.sample return list. We access first/only element.
        self._dealt.append(sample[0])
        return self._deck[sample[0]]

    def reset_deck(self) -> None:
        self._dealt.clear()

    def print_deck(self) -> None:
        for i, card in self._deck.items():
            print(i, str(card))


class Player:
    """
    Represents a player in a card game.

    Attributes:
        _name (str): The player's name
    """

    def __init__(self, name: str) -> None:
        self._name = name


class PokerGame:
    """
    Manages a poker game session.

    Handles game setup, player management, dealing cards, and determining winners.
    Supports both 5-card draw and 5-card stud variants.

    Attributes:
        _draw (bool): True if playing 5-card draw, False for 5-card stud
        _num_players (int): Number of players in the game
        _deck (Deck): The game's deck of cards
        _players (dict[Player, PokerHand]): Maps players to their poker hands
    """

    def __init__(self) -> None:
        self._draw = False
        self._num_players = 0
        while True:
            ans = input("\nWill this be a game of 5 card draw? y/n: ")
            if ans in {"y", "Y", "n", "N"}:
                if ans.lower() == "y":
                    self._draw = True
                break
            else:
                print("You must enter y or n")
                input("Press Enter to continue...")

        while True:
            ans = input("Enter the number of players: ")
            try:
                self._num_players = int(ans)
            except ValueError:
                print("Invalid input. Please enter a number")
                input("Press Enter to continue...")
                continue

            if self._num_players < 2:
                print("There must be at leat 2 players in a game\n")
                continue
            if self._draw and self._num_players > 6:
                print("There must be 2 to 6 players in a game of 5 card draw\n")
                continue
            elif self._num_players > 10:
                print("There must be 2 to 10 players in a game of 5 card stud\n")
                continue

            break

        self._deck: Deck = Deck()
        self._players: dict[Player, PokerHand | None] = {}
        self.add_players(self._num_players)

    def add_players(self, num_players: int) -> None:
        for _ in range(num_players):
            name = input("Enter a player's name: ")
            self._players[Player(name)] = None

    def deal_cards(self, hand_size: int) -> None:
        for player in self._players:
            hand = self._deck.random_deal(hand_size)
            self._players[player] = PokerHand(hand)

    def show_hand(self, player: Player) -> None:
        hand = self._players[player]
        if hand:
            print(f"{player._name} with ", end="")
            match hand._hand_value[0]:
                case PokerHand.ROYAL_FLUSH:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.rank)
                    print("Royal Flush:", " ".join(str(card) for card in sorted_cards))

                case PokerHand.STRAIGHT_FLUSH:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.rank)
                    print("Straight Flush:", " ".join(str(card) for card in sorted_cards))

                case PokerHand.FOUR_OF_A_KIND:
                    # Group four matching cards first, then the remaining card
                    four_value = hand._hand_value[1]
                    four_cards = [card for card in hand._cards if card.rank == four_value]
                    other_card = [card for card in hand._cards if card.rank != four_value]
                    print(
                        "Four of a Kind:",
                        " ".join(str(card) for card in four_cards + other_card),
                    )

                case PokerHand.FULL_HOUSE:
                    # Group three matching cards first, then the pair
                    three_value = hand._hand_value[1]
                    pair_value = hand._hand_value[2]
                    three_cards = [card for card in hand._cards if card.rank == three_value]
                    pair_cards = [card for card in hand._cards if card.rank == pair_value]
                    print(
                        "Full House:",
                        " ".join(str(card) for card in three_cards + pair_cards),
                    )

                case PokerHand.FLUSH:
                    # Sort by value since they're all the same suit
                    sorted_cards = sorted(hand._cards, key=lambda x: x.rank, reverse=True)
                    print("Flush:", " ".join(str(card) for card in sorted_cards))

                case PokerHand.STRAIGHT:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.rank)
                    print("Straight:", " ".join(str(card) for card in sorted_cards))

                case PokerHand.THREE_OF_A_KIND:
                    three_value = hand._hand_value[1]
                    three_cards = [card for card in hand._cards if card.rank == three_value]
                    other_cards = sorted(
                        [card for card in hand._cards if card.rank != three_value],
                        key=lambda x: x.rank,
                        reverse=True,
                    )
                    print(
                        "Three of a Kind:",
                        " ".join(str(card) for card in three_cards + other_cards),
                    )

                case PokerHand.TWO_PAIR:
                    high_pair = hand._hand_value[1]
                    low_pair = hand._hand_value[2]
                    high_pair_cards = [card for card in hand._cards if card.rank == high_pair]
                    low_pair_cards = [card for card in hand._cards if card.rank == low_pair]
                    other_card = [card for card in hand._cards if card.rank not in (high_pair, low_pair)]
                    print(
                        "Two Pair:",
                        " ".join(str(card) for card in high_pair_cards + low_pair_cards + other_card),
                    )

                case PokerHand.ONE_PAIR:
                    pair_value = hand._hand_value[1]
                    pair_cards = [card for card in hand._cards if card.rank == pair_value]
                    other_cards = sorted(
                        [card for card in hand._cards if card.rank != pair_value],
                        key=lambda x: x.rank,
                        reverse=True,
                    )
                    print(
                        "One Pair:",
                        " ".join(str(card) for card in pair_cards + other_cards),
                    )

                case PokerHand.HIGH_CARD:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.rank, reverse=True)
                    print("High Card:", " ".join(str(card) for card in sorted_cards))

    def show_players_hand(self, player):
        self.show_hand(player)

    def show_all_hands(self) -> None:
        for player in self._players.keys():
            print(f"\n{player._name}, please have a seat")
            input("Press Enter when you are ready to see your cards ...")
            self.show_hand(player)
            input("Press Enter when you are done seeing your cards ...")
            # Clear terminal screen
            os.system("cls" if os.name == "nt" else "clear")

    def draw_cards(self) -> None:
        for player in self._players:
            num_cards_trading = 0
            print(f"\n{player._name}, please have a seat")
            input("Press Enter when you are ready to see your cards ...")
            self.show_hand(player)
            while True:
                ans = input(f"\n{player._name}, how many cards are you trading in (0-3)? ")
                try:
                    num_cards_trading = int(ans)
                except ValueError:
                    print("Invalid input. Please enter a number")
                    input("Press Enter to continue ...")
                    continue

                if not 0 <= num_cards_trading <= 3:
                    print("You must enter a number from 0 to 3")
                    input("Press Enter to continue ...")
                    continue
                else:
                    break

            curr_num_cards = 0
            while curr_num_cards < num_cards_trading:
                trade = input("\nEnter the card you are trading (e.g. qh for Q♥ or 10c for 10♣): ")
                if len(trade) == 2:
                    rank, suit = trade[0], trade[1]
                elif len(trade) == 3 and trade.startswith("10"):
                    rank, suit = "10", trade[2]
                else:
                    print("\nInvalid card format. Please enter two characters\n" "(e.g. qh for Q♥ or 10c for 10♣): ")
                    input("Press Enter to continue ...")
                    continue

                # Get the player's hand.
                player_hand = self._players[player]

                # Check if player has a valid hand.
                if player_hand is None:
                    print(f"Player {player._name} has no hand")
                    continue

                # Is trade is a valid card?
                if rank in Card.RANK_DICT and suit in Card.SUIT_SET:
                    # If the player is holding this card, remove the card from the players hand.
                    if player_hand.remove_card(Card.RANK_DICT[rank], suit):
                        new_card = self._deck.random_deal_one()
                        player_hand.add_card(new_card)
                        player_hand.update_best_hand()
                        curr_num_cards += 1
                    else:
                        # Use uppercase for face cards and Ace, and get the Unicode suit symbol
                        rank_display = rank.upper() if rank in {"j", "q", "k", "a"} else rank
                        suit_symbol = Card.SUIT_SYMBOLS[suit]
                        print(f"{player._name} does not have a {rank_display}{suit_symbol}")
                        input("Press Enter to continue ...")
                else:
                    print("\nInvalid card. Please enter a valid card value and suit.")
                    input("Press Enter to continue ...")

            print("\nYour final hand:")
            self.show_hand(player)
            input("\nPress Enter when you are done seeing your cards ...")
            # Clear terminal screen
            os.system("cls" if os.name == "nt" else "clear")

    def winners(self) -> set:
        curr_winners = set()
        curr_winning_hand = None

        for player, hand in self._players.items():
            # Skip if current hand is None
            if hand is None:
                continue

            # The first player with a valid hand is the initial winner.
            if len(curr_winners) == 0 or curr_winning_hand is None:
                curr_winners.add(player)
                curr_winning_hand = hand
            elif hand > curr_winning_hand:
                curr_winners = {player}
                curr_winning_hand = hand
            elif hand == curr_winning_hand:
                curr_winners.add(player)

        return curr_winners


if __name__ == "__main__":
    game = PokerGame()
    game.deal_cards(5)

    if game._draw:
        game.draw_cards()
    else:
        game.show_all_hands()

    winners = game.winners()
    input("Press enter to reveal the WINNER!")
    print("\nAnd the winner is ... ")
    if len(winners) > 1:
        print("There is a tie between:")
        for player in winners:
            game.show_hand(player)
    else:
        game.show_hand(next(iter(winners)))

    print("\nThe loser(s) are:")
    for player in game._players:
        if player not in winners:
            game.show_hand(player)
