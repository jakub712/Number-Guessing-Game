# 🎯 Number Guessing Game (Python CLI Edition)

This is a simple but polished number guessing game built in pure Python. It includes colored output, input validation, win streak tracking, and a “play again” option — all inside the terminal.

---

## 🕹️ Features

- Player chooses difficulty: Easy, Medium, or Hard
- Game picks a number between 1–100
- Colored feedback for:
  - ✅ Correct guess
  - 🔼 Too high
  - 🔽 Too low
  - ❌ Invalid input
- Input validation (no crashes from letters or bad input)
- Win streak tracker
- “Play again?” option
- Clean console layout with emoji reactions

---

## 📸 Sample Output

😈 Difficulty set to Easy. You have 15 guesses.
Let's test your luck! Pick a number between 1 and 100:

❌ Too low! Try again.
🔽 Too low!
🔼 Too high!
✅ You guessed it! The number was 42.
🔥 Current win streak: 3

Play again? (y/n):


---

## 🧠 What This Project Demonstrates

- Conditionals and loops
- `try/except` input validation
- Colored console output using `colorama`
- Game flow control (`while True` loops)
- State tracking (streaks, guesses)
- Beginner-friendly terminal UX polish

---

## ▶️ How to Run It

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game

2. Install required module:

pip install colorama

3. Run the game:

python3 guess.py

🧪 Difficulty Settings
Mode	Guesses
Easy	15
Medium	10
Hard	5
💬 Author

Built with 💻 and 🎯 by Jakub Lesniak
Part of my "50 Projects in 50 Days" Python challenge.

📲 Follow my journey on TikTok → @jakub_codes
