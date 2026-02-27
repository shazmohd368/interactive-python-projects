# Stopwatch: The Game

Mini project from:
"An Introduction to Interactive Programming in Python" – Rice University

## 📌 Description

A stopwatch game where the player attempts to stop the timer on whole seconds.

Score format:
x / y

- x → Successful stops on whole seconds
- y → Total stop attempts

## 🧠 Concepts Used

- Event-driven programming
- Timer events (0.1 second interval)
- Global state tracking
- Game scoring logic
- simplegui framework
- Time formatting logic (A:BC.D)

## 🎮 Game Logic

- Timer runs in tenths of seconds.
- When stopped:
  - If stopped exactly on a whole second → score increases.
  - Otherwise → only attempt count increases.
- Reset clears time and score.

## ▶️ How to Run

This project uses the `simplegui` module from CodeSkulptor.

To run:
1. Open CodeSkulptor.
2. Paste the contents of `main.py`.
3. Click Run.

⚠️ Note: `simplegui` is not part of standard Python and will not run locally without modification.
