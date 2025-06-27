import pytest
from poker_game import Card, PokerHand, Deck, Player, PokerGame


@pytest.fixture
def sample_cards_royal_flush():
    return [
        Card("a", "h"),
        Card("k", "h"),
        Card("q", "h"),
        Card("j", "h"),
        Card("10", "h"),
    ]


@pytest.fixture
def sample_cards_four_kind():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("a", "c"),
        Card("a", "s"),
        Card("k", "h"),
    ]


@pytest.fixture
def sample_cards_straight_flush():
    return [
        Card("9", "c"),
        Card("8", "c"),
        Card("7", "c"),
        Card("6", "c"),
        Card("5", "c"),
    ]


@pytest.fixture
def sample_cards_full_house():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("a", "c"),
        Card("k", "h"),
        Card("k", "d"),
    ]


@pytest.fixture
def sample_cards_flush():
    return [
        Card("a", "h"),
        Card("j", "h"),
        Card("9", "h"),
        Card("7", "h"),
        Card("4", "h"),
    ]


@pytest.fixture
def sample_cards_straight():
    return [
        Card("9", "h"),
        Card("8", "c"),
        Card("7", "d"),
        Card("6", "s"),
        Card("5", "h"),
    ]


@pytest.fixture
def sample_cards_three_kind():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("a", "c"),
        Card("k", "h"),
        Card("q", "d"),
    ]


@pytest.fixture
def sample_cards_two_pair():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("k", "c"),
        Card("k", "h"),
        Card("q", "d"),
    ]


@pytest.fixture
def sample_cards_one_pair():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("k", "c"),
        Card("q", "h"),
        Card("j", "d"),
    ]


@pytest.fixture
def sample_cards_high_card():
    return [
        Card("a", "h"),
        Card("k", "d"),
        Card("q", "c"),
        Card("j", "h"),
        Card("9", "d"),
    ]


@pytest.fixture
def tied_royal_flush_hearts():
    return [
        Card("a", "h"),
        Card("k", "h"),
        Card("q", "h"),
        Card("j", "h"),
        Card("10", "h"),
    ]


@pytest.fixture
def tied_royal_flush_spades():
    return [
        Card("a", "s"),
        Card("k", "s"),
        Card("q", "s"),
        Card("j", "s"),
        Card("10", "s"),
    ]


@pytest.fixture
def tied_straight_flush_high():
    return [
        Card("k", "h"),
        Card("q", "h"),
        Card("j", "h"),
        Card("10", "h"),
        Card("9", "h"),
    ]


@pytest.fixture
def tied_straight_flush_high_diff_suit():
    return [
        Card("k", "d"),
        Card("q", "d"),
        Card("j", "d"),
        Card("10", "d"),
        Card("9", "d"),
    ]


@pytest.fixture
def tied_full_house():
    return [
        Card("k", "h"),
        Card("k", "d"),
        Card("k", "c"),
        Card("q", "h"),
        Card("q", "d"),
    ]


@pytest.fixture
def tied_full_house_diff_pair():
    return [
        Card("k", "h"),
        Card("k", "d"),
        Card("k", "s"),
        Card("j", "h"),
        Card("j", "d"),
    ]


@pytest.fixture
def tied_flush_hearts():
    return [
        Card("a", "h"),
        Card("k", "h"),
        Card("j", "h"),
        Card("9", "h"),
        Card("7", "h"),
    ]


@pytest.fixture
def tied_flush_hearts_diff():
    return [
        Card("a", "h"),
        Card("k", "h"),
        Card("j", "h"),
        Card("9", "h"),
        Card("6", "h"),
    ]


@pytest.fixture
def tied_straight():
    return [
        Card("9", "h"),
        Card("8", "c"),
        Card("7", "d"),
        Card("6", "s"),
        Card("5", "h"),
    ]


@pytest.fixture
def tied_straight_diff_suits():
    return [
        Card("9", "d"),
        Card("8", "h"),
        Card("7", "s"),
        Card("6", "c"),
        Card("5", "d"),
    ]


@pytest.fixture
def tied_three_kind():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("q", "c"),
        Card("j", "h"),
        Card("9", "d"),
    ]


@pytest.fixture
def tied_three_kind_diff_kickers():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("q", "s"),
        Card("j", "h"),
        Card("8", "d"),
    ]


@pytest.fixture
def tied_two_pair():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("j", "c"),
        Card("j", "h"),
        Card("9", "d"),
    ]


@pytest.fixture
def tied_two_pair_diff_kicker():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("j", "c"),
        Card("j", "h"),
        Card("8", "d"),
    ]


@pytest.fixture
def tied_one_pair():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("j", "c"),
        Card("9", "h"),
        Card("7", "d"),
    ]


@pytest.fixture
def tied_one_pair_diff_kickers():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("j", "c"),
        Card("9", "h"),
        Card("6", "d"),
    ]


@pytest.fixture
def tied_high_card():
    return [
        Card("a", "h"),
        Card("k", "d"),
        Card("j", "c"),
        Card("9", "h"),
        Card("7", "d"),
    ]


@pytest.fixture
def tied_high_card_2():
    return [
        Card("a", "h"),
        Card("k", "d"),
        Card("j", "c"),
        Card("9", "h"),
        Card("7", "d"),
    ]


@pytest.fixture
def sample_high_card_ace():
    return [
        Card("a", "h"),
        Card("k", "d"),
        Card("j", "c"),
        Card("9", "h"),
        Card("6", "d"),
    ]


@pytest.fixture
def sample_four_kind_aces():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("a", "c"),
        Card("a", "s"),
        Card("k", "h"),
    ]


@pytest.fixture
def sample_four_kind_kings():
    return [
        Card("k", "h"),
        Card("k", "d"),
        Card("k", "c"),
        Card("k", "s"),
        Card("a", "h"),
    ]


@pytest.fixture
def sample_four_kind_same_kicker():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("a", "c"),
        Card("a", "s"),
        Card("k", "d"),
    ]


@pytest.fixture
def sample_add_remove_cards():
    return [
        Card("a", "h"),
        Card("a", "d"),
        Card("a", "c"),
        Card("k", "h"),
        Card("3", "d"),
    ]


@pytest.fixture
def sample_flush_hearts():
    return [
        Card("a", "h"),
        Card("k", "h"),
        Card("j", "h"),
        Card("9", "h"),
        Card("7", "h"),
    ]


@pytest.fixture
def sample_flush_spades():
    return [
        Card("a", "s"),
        Card("k", "s"),
        Card("j", "s"),
        Card("9", "s"),
        Card("7", "s"),
    ]


@pytest.fixture
def sample_three_kind_queens():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("q", "c"),
        Card("j", "h"),
        Card("9", "d"),
    ]


@pytest.fixture
def sample_two_pair_queens_jacks():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("j", "c"),
        Card("j", "h"),
        Card("9", "d"),
    ]


@pytest.fixture
def sample_one_pair_queens():
    return [
        Card("q", "h"),
        Card("q", "d"),
        Card("j", "c"),
        Card("9", "h"),
        Card("7", "d"),
    ]


def test_card_creation():
    card = Card("a", "h")
    assert card.rank == Card.RANK_DICT["a"]
    assert card.suit == "h"
    assert str(card) == "A♥"


def test_card_comparison():
    card1 = Card("a", "h")
    card2 = Card("k", "h")
    assert card2.rank < card1.rank
    assert not (card1.rank < card2.rank)


def test_poker_hand_royal_flush(sample_cards_royal_flush):
    hand = PokerHand(sample_cards_royal_flush)
    assert hand._hand_value[0] == 10  # ROYAL_FLUSH


def test_poker_hand_straight_flush(sample_cards_straight_flush):
    hand = PokerHand(sample_cards_straight_flush)
    assert hand._hand_value[0] == 9  # STRAIGHT_FLUSH


def test_poker_hand_four_kind(sample_cards_four_kind):
    hand = PokerHand(sample_cards_four_kind)
    assert hand._hand_value[0] == 8  # FOUR_OF_A_KIND


def test_poker_hand_full_house(sample_cards_full_house):
    hand = PokerHand(sample_cards_full_house)
    assert hand._hand_value[0] == 7  # FULL_HOUSE


def test_poker_hand_flush(sample_cards_flush):
    hand = PokerHand(sample_cards_flush)
    assert hand._hand_value[0] == 6  # FLUSH


def test_poker_hand_straight(sample_cards_straight):
    hand = PokerHand(sample_cards_straight)
    assert hand._hand_value[0] == 5  # STRAIGHT


def test_poker_hand_three_kind(sample_cards_three_kind):
    hand = PokerHand(sample_cards_three_kind)
    assert hand._hand_value[0] == 4  # THREE_OF_A_KIND


def test_poker_hand_two_pair(sample_cards_two_pair):
    hand = PokerHand(sample_cards_two_pair)
    assert hand._hand_value[0] == 3  # TWO_PAIR


def test_poker_hand_one_pair(sample_cards_one_pair):
    hand = PokerHand(sample_cards_one_pair)
    assert hand._hand_value[0] == 2  # ONE_PAIR


def test_poker_hand_high_card(sample_cards_high_card):
    hand = PokerHand(sample_cards_high_card)
    assert hand._hand_value[0] == 1  # HIGH_CARD


def test_poker_hand_comparison(sample_cards_royal_flush, sample_cards_four_kind):
    royal_flush = PokerHand(sample_cards_royal_flush)
    four_kind = PokerHand(sample_cards_four_kind)
    assert four_kind < royal_flush
    assert not (royal_flush < four_kind)


def test_deck_creation():
    deck = Deck()
    # Standard deck should have 52 cards
    assert len(deck._deck) == 52
    # No cards should be dealt initially
    assert len(deck._dealt) == 0


def test_deck_dealing():
    deck = Deck()
    hand = deck.random_deal(5)
    assert len(hand) == 5
    assert len(deck._dealt) == 5
    # Cards should be unique
    values = [(card.rank, card.suit) for card in hand]
    assert len(set(values)) == 5


def test_deck_deal_one():
    deck = Deck()
    card = deck.random_deal_one()
    assert isinstance(card, Card)
    assert len(deck._dealt) == 1


def test_deck_reset():
    deck = Deck()
    deck.random_deal(5)
    assert len(deck._dealt) == 5
    deck.reset_deck()
    assert len(deck._dealt) == 0


def test_player_creation():
    player = Player("Test Player")
    assert player._name == "Test Player"


@pytest.fixture
def mock_input(monkeypatch):
    inputs = iter(["n", "2", "Player1", "Player2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))


def test_poker_game_creation(mock_input):
    game = PokerGame()
    assert game._draw is False
    assert len(game._players) == 2


def test_poker_game_deal_cards(mock_input):
    game = PokerGame()
    game.deal_cards(5)
    # Each player should have a hand
    assert all(hand is not None for hand in game._players.values())
    # Each hand should have 5 cards
    assert all(len(hand._cards) == 5 for hand in game._players.values() if hand)


def test_poker_hand_add_remove_card(sample_add_remove_cards):
    hand = PokerHand(sample_add_remove_cards)

    # Test removing a card
    assert hand.remove_card(3, "d") is True
    assert len(hand._cards) == 4

    # Test removing a non-existent card
    assert hand.remove_card("2", "h") is False

    # Test adding a card
    new_card = Card("a", "s")
    hand.add_card(new_card)
    assert len(hand._cards) == 5
    assert new_card in hand._cards


@pytest.fixture
def mock_draw_input(monkeypatch):
    inputs = iter(["y", "2", "Player1", "Player2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))


def test_poker_game_draw_mode(mock_draw_input):
    game = PokerGame()
    assert game._draw is True
    assert len(game._players) == 2


def test_poker_game_winner(mock_input):
    game = PokerGame()
    game.deal_cards(5)
    winners = game.winners()
    a_winner = next(iter(winners))
    assert isinstance(a_winner, Player)
    assert a_winner in game._players.keys()


def test_poker_game_draw_winners(mock_input, tied_royal_flush_hearts, tied_royal_flush_spades):
    game = PokerGame()
    # Manually set player hands to equal royal flushes
    players = list(game._players.keys())
    game._players[players[0]] = PokerHand(tied_royal_flush_hearts)
    game._players[players[1]] = PokerHand(tied_royal_flush_spades)

    winners = game.winners()
    assert len(winners) == 2  # Both players should be winners
    assert all(player in game._players.keys() for player in winners)


def test_poker_hand_comparison_order(
    sample_cards_royal_flush,
    sample_cards_straight_flush,
    sample_cards_four_kind,
    sample_cards_full_house,
    sample_cards_flush,
    sample_cards_straight,
    sample_cards_two_pair,
    sample_cards_three_kind,
    sample_cards_one_pair,
    sample_cards_high_card,
):
    royal_flush = PokerHand(sample_cards_royal_flush)
    straight_flush = PokerHand(sample_cards_straight_flush)
    four_kind = PokerHand(sample_cards_four_kind)
    full_house = PokerHand(sample_cards_full_house)
    flush = PokerHand(sample_cards_flush)
    straight = PokerHand(sample_cards_straight)
    three_kind = PokerHand(sample_cards_three_kind)
    two_pair = PokerHand(sample_cards_two_pair)
    one_pair = PokerHand(sample_cards_one_pair)
    high_card = PokerHand(sample_cards_high_card)

    # Test the poker hand hierarchy
    assert royal_flush > straight_flush
    assert straight_flush < royal_flush
    assert straight_flush > four_kind
    assert four_kind < straight_flush
    assert four_kind > full_house
    assert full_house < four_kind
    assert full_house > flush
    assert flush < full_house
    assert flush > straight
    assert straight < flush
    assert straight > three_kind
    assert three_kind < straight
    assert three_kind > two_pair
    assert two_pair < three_kind
    assert two_pair > one_pair
    assert one_pair < two_pair
    assert one_pair > high_card
    assert high_card < one_pair


def test_poker_hand_same_rank_comparison(sample_four_kind_aces, sample_four_kind_kings):
    hand1 = PokerHand(sample_four_kind_aces)
    hand2 = PokerHand(sample_four_kind_kings)
    assert hand2 < hand1


def test_hand_get_hand_representation(sample_cards_royal_flush):
    hand = PokerHand(sample_cards_royal_flush)
    hand_repr = hand.get_hand
    assert isinstance(hand_repr, list)
    assert hand_repr[0] == 10
    assert all(isinstance(card_str, str) for card_str in hand_repr[1:])
    assert len(hand_repr) == 6  # Hand type + 5 cards


def test_poker_hand_royal_flush_tie(tied_royal_flush_hearts, tied_royal_flush_spades):
    hand1 = PokerHand(tied_royal_flush_hearts)
    hand2 = PokerHand(tied_royal_flush_spades)
    # Royal flushes of different suits should tie
    assert not (hand1 < hand2)
    assert not (hand2 < hand1)


def test_poker_hand_straight_flush_tie(
    tied_straight_flush_high, tied_straight_flush_high_diff_suit
):
    hand1 = PokerHand(tied_straight_flush_high)
    hand2 = PokerHand(tied_straight_flush_high_diff_suit)
    # Same high cards in straight flush should tie regardless of suit
    assert not (hand1 < hand2)
    assert not (hand2 < hand1)


def test_poker_hand_full_house_tie(tied_full_house, tied_full_house_diff_pair):
    hand1 = PokerHand(tied_full_house)  # Kings full of Queens
    hand2 = PokerHand(tied_full_house_diff_pair)  # Kings full of Jacks
    # Same three of a kind in full house, higher pair should win
    assert hand2 < hand1
    assert not (hand1 < hand2)


def test_poker_hand_flush_tie(tied_flush_hearts, tied_flush_hearts_diff):
    hand1 = PokerHand(tied_flush_hearts)  # A K J 9 7
    hand2 = PokerHand(tied_flush_hearts_diff)  # A K J 9 6
    # Compare each card from highest to lowest until difference found
    assert hand2 < hand1
    assert not (hand1 < hand2)


def test_poker_hand_straight_tie(tied_straight, tied_straight_diff_suits):
    hand1 = PokerHand(tied_straight)
    hand2 = PokerHand(tied_straight_diff_suits)
    # Same high card in straight should tie regardless of suits
    assert not (hand1 < hand2)
    assert not (hand2 < hand1)


def test_poker_hand_three_kind_tie(tied_three_kind, tied_three_kind_diff_kickers):
    hand1 = PokerHand(tied_three_kind)  # Queens with J 9
    hand2 = PokerHand(tied_three_kind_diff_kickers)  # Queens with J 8
    # Same three of a kind, compare kickers
    assert hand2 < hand1
    assert not (hand1 < hand2)


def test_poker_hand_two_pair_tie(tied_two_pair, tied_two_pair_diff_kicker):
    hand1 = PokerHand(tied_two_pair)  # Q Q J J 9
    hand2 = PokerHand(tied_two_pair_diff_kicker)  # Q Q J J 8
    # Same two pairs, compare kicker
    assert hand2 < hand1
    assert not (hand1 < hand2)


def test_poker_hand_one_pair_tie(tied_one_pair, tied_one_pair_diff_kickers):
    hand1 = PokerHand(tied_one_pair)  # Q Q J 9 7
    hand2 = PokerHand(tied_one_pair_diff_kickers)  # Q Q J 9 6
    # Same pair, compare remaining cards in order
    assert hand2 < hand1
    assert not (hand1 < hand2)


def test_poker_hand_high_card_tie(tied_high_card, sample_high_card_ace):
    hand1 = PokerHand(tied_high_card)  # A K J 9 7
    hand2 = PokerHand(sample_high_card_ace)  # A K J 9 6
    # Compare each card from highest to lowest
    assert hand2 < hand1
    assert not (hand1 < hand2)


def test_poker_hand_royal_flush_equal(tied_royal_flush_hearts, tied_royal_flush_spades):
    hand1 = PokerHand(tied_royal_flush_hearts)
    hand2 = PokerHand(tied_royal_flush_spades)
    # Royal flushes are always equal regardless of suit
    assert hand1 == hand2


def test_poker_hand_straight_flush_equal(
    tied_straight_flush_high, tied_straight_flush_high_diff_suit
):
    hand1 = PokerHand(tied_straight_flush_high)
    hand2 = PokerHand(tied_straight_flush_high_diff_suit)
    # Same rank straight flushes are equal regardless of suit
    assert hand1 == hand2


def test_poker_hand_four_kind_equal(sample_four_kind_aces, sample_four_kind_same_kicker):
    hand1 = PokerHand(sample_four_kind_aces)
    hand2 = PokerHand(sample_four_kind_same_kicker)
    # Four of a kind with same kicker value are equal regardless of kicker suit
    assert hand1 == hand2


def test_poker_hand_straight_equal(tied_straight, tied_straight_diff_suits):
    hand1 = PokerHand(tied_straight)
    hand2 = PokerHand(tied_straight_diff_suits)
    # Same rank straights are equal regardless of suit
    assert hand1 == hand2


def test_poker_hand_flush_equal(sample_flush_hearts, sample_flush_spades):
    hand1 = PokerHand(sample_flush_hearts)
    hand2 = PokerHand(sample_flush_spades)
    # Equal flush hands
    assert hand1 == hand2


def test_poker_hand_three_kind_equal(tied_three_kind, sample_three_kind_queens):
    hand1 = PokerHand(sample_three_kind_queens)
    hand2 = PokerHand(tied_three_kind)  # Same cards but potentially different order
    # Same rank three of a kind with same kickers are equal regardless of suit
    assert hand1 == hand2


def test_poker_hand_two_pair_equal(tied_two_pair, sample_two_pair_queens_jacks):
    hand1 = PokerHand(sample_two_pair_queens_jacks)
    hand2 = PokerHand(tied_two_pair)  # Same cards but potentially different order
    # Same rank two pairs with same kicker are equal regardless of suit
    assert hand1 == hand2


def test_poker_hand_one_pair_equal(tied_one_pair, sample_one_pair_queens):
    hand1 = PokerHand(sample_one_pair_queens)
    hand2 = PokerHand(tied_one_pair)  # Same cards but potentially different order
    # Same rank pairs with same kickers are equal regardless of suit
    assert hand1 == hand2


def test_poker_hand_high_card_equal(tied_high_card, tied_high_card_2):
    hand2 = PokerHand(tied_high_card)  # A K J 9 6
    hand1 = PokerHand(tied_high_card_2)  # A K J 9 6
    # All cards are the same, so they are equal
    assert hand1 == hand2


def test_poker_hand_high_card_equal_2(tied_high_card, sample_high_card_ace):
    hand1 = PokerHand(tied_high_card)  # A K J 9 6
    hand2 = PokerHand(sample_high_card_ace)  # A K J 9 7
    assert hand1 != hand2


def test_poker_hand_not_equal(sample_cards_royal_flush, sample_cards_four_kind):
    royal_flush = PokerHand(sample_cards_royal_flush)
    four_kind = PokerHand(sample_cards_four_kind)
    # Different hand types are not equal
    assert royal_flush != four_kind
