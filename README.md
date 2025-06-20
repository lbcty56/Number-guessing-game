🔢 Guess My Number! (Console Game)
A classic "Guess the Number" game implemented in Python, playable directly in your console. This project provides a practical demonstration of fundamental programming concepts, robust user interaction, and clean code practices.

✨ Features
Secret Number Generation: A random number between 1 and 100 is chosen for each round.
Adjustable Difficulty: Players can choose 'easy' (10 attempts) or 'hard' (5 attempts).
Interactive Guessing: Provides feedback ("Too high," "Too low") after each guess.
Robust Input Validation: Ensures user input for difficulty and new rounds is valid.
Attempt Tracking: Clearly displays remaining attempts to the player.
Win/Loss Conditions: Detects correct guesses for a win or announces loss upon exhausting attempts.
Play Again Option: Seamlessly allows players to start new rounds without restarting the script.
🛠️ Technologies & Skills Demonstrated
This project showcases foundational to intermediate Python development skills:

Python Fundamentals: Strong command of variables, data types (integers, strings), conditional statements (if/elif/else), and looping constructs (for, while) for robust game logic and flow control.
Modular Programming & Function Design: Employed a highly functional design with well-defined, single-responsibility functions (e.g., start_msg, game_logic, new_round_msg). This promotes code readability, maintainability, and reusability.
User Input & Validation: Implemented effective console-based input (input()) and crucial validation loops (while difficulty not in [...]) to prevent invalid user input from breaking the program, enhancing user experience and program stability.
Game Logic Implementation: Developed the core guessing algorithm, including attempt management, range checks, and win/loss conditions.
Randomization: Utilized the random module (random.randint) to ensure a fair and unpredictable secret number for each game.
Console Output & Formatting: Effective use of print() statements and f-strings for clear, dynamic, and engaging user feedback.
Code Organization: Structured the entire game within a main number_guessing_game() function, demonstrating good program entry point and overall organization.
(Note for Self-Improvement: For a future iteration, consider adding try-except ValueError around int(input("Make a guess: ")) to handle cases where the user types non-numeric characters, making the input even more robust.)

🚀 How to Run
Clone the repository:
Bash

git clone https://github.com/YourUsername/your-number-guessing-game.git
cd your-number-guessing-game
Ensure art module is installed:
Bash

pip install art
Run the game:
Bash

python game.py
