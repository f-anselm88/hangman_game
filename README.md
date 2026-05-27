# 🪢 Hangman

A fully playable command-line Hangman game built in Python, featuring progressive ASCII art, dynamic word masking, and a complete win/loss system.

---

## Features

- ✅ Progressive ASCII hangman art tied to incorrect guess count
- ✅ Dynamic word masking that reveals letters as you guess correctly
- ✅ Tracks used letters to prevent duplicate guesses
- ✅ Win and loss detection with replay option
- ✅ Built-in word bank with random word selection

---

## Demo

```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

Word: _ _ _ _ _ _ _
Used letters: A, E, T

Guess a letter: p

Word: _ _ P _ _ _ _
Correct! Nice guess.
```

---

## How to Run

**Requirements:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/f-anselm88/hangman.git

# Navigate into the project
cd hangman

# Run the program
python hangman.py
```

---

## How It Works

1. A random word is selected from the word bank
2. The word is displayed as underscores (`_ _ _ _`)
3. The player guesses one letter at a time
4. Correct guesses reveal the letter in the word
5. Incorrect guesses add a body part to the ASCII art (6 allowed)
6. The game ends when the word is complete or the man is fully drawn

---

## ASCII Art Progression

| Incorrect Guesses | State |
|:-:|---|
| 0 | Empty gallows |
| 1 | Head added |
| 2 | Body added |
| 3 | Left arm added |
| 4 | Right arm added |
| 5 | Left leg added |
| 6 | Right leg — Game Over |

---

## What I Learned

- Managing game state across multiple rounds with loops and flags
- String manipulation for dynamic word masking
- Organizing multi-stage ASCII art rendering with conditionals

---

## Author

**Anselm Munango**
[f-anselm88.github.io](https://f-anselm88.github.io) · [GitHub](https://github.com/f-anselm88) · [LinkedIn](https://linkedin.com/in/anselm-munango-bs) · [anselm.mu@gmail.com](mailto:anselm.mu@gmail.com)
