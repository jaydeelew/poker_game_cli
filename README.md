# Poker Game CLI

A command-line Poker game built with Python. The game supports both 5-card draw and 5-card stud variants, allowing multiple players to join, play, and determine the winner based on standard poker hand rankings.

---

## Features

- **Command-Line Interface**: Play poker directly in your terminal.
- **Poker Variants**: Play 5-card draw or 5-card stud.
- **Multiple Players**: Add or remove players before starting a game.
- **Hand Evaluation**: Automatic hand ranking and winner determination.
- **Card Exchange**: In 5-card draw, exchange up to 3 cards per player.

---

## Gameplay Overview

- **Add Players**: Enter player names and add at least two players.
- **Choose Variant**: Select between 5 Card Draw or 5 Card Stud at the start.
- **Deal Cards**: The game deals cards to all players.
- **Card Exchange**: In draw poker, players may exchange up to 3 cards.
- **Reveal Winner**: The game determines and displays the winner and all hands.
- **Restart**: Option to play again after a game ends.

### Supported Poker Hands

- Royal Flush
- Straight Flush
- Four of a Kind
- Full House
- Flush
- Straight
- Three of a Kind
- Two Pair
- One Pair
- High Card

---

## Installation

> **Note:** Python 3.10 or higher is required.

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/jaydeelew/poker_game_cli.git
   cd poker_game_cli
   ```

2. **(Optional) Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

To play the game, execute the following command from the root directory of the project:

```bash
python3 ./src/poker_game.py
```

Follow the on-screen prompts to add players, select the game variant, and play Poker in your terminal!

---

I am happy to receive advice for improvements.

---
