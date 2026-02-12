## Example Output

# Rock Paper Scissors Lizard Spock

Mini project from the course:
"An Introduction to Interactive Programming in Python"

## 📌 Description
An extended version of the classic Rock-Paper-Scissors game with five choices:
Rock, Paper, Scissors, Lizard, and Spock.

The winner is determined using modulo arithmetic to simplify comparison logic between cyclic choices.

## 🧠 Concepts Used
- Functions
- Conditional statements
- Mapping strings to numbers
- Modulo arithmetic
- Random module
- Basic input validation

## ⚙️ How It Works

Each choice is mapped to a number:

0 → rock  
1 → Spock  
2 → paper  
3 → lizard  
4 → scissors  

Winner is calculated using:

(player_number - computer_number) % 5

If result is:
- 0 → Tie
- 1 or 2 → Player wins
- 3 or 4 → Computer wins

## ▶️ Example Output

Player chooses rock
Computer chooses Spock
Computer wins!

Player chooses Spock
Computer chooses Spock
Player and computer tie!

Player chooses paper
Computer chooses rock
Player wins!

Player chooses lizard
Computer chooses Spock
Player wins!

Player chooses scissors
Computer chooses paper
Player wins!

Player chooses sheldon
invalid input


## 🚀 What I Learned
- How to simplify complex conditional logic using mathematics
- Structuring a small interactive Python program
- Separating logic into reusable functions


## ▶️ How to Run

Make sure Python 3 is installed.


Run the program using:

```bash
python main.py
