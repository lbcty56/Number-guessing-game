import random
import art

def start_msg(answer):
    print(art.logo)
    print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 to 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty not in ["easy","hard"]:
        difficulty = input("Invalid choice. Type 'easy' or 'hard': ").lower()
    return difficulty

def attempt_for_guessing(difficulty):
    if difficulty == "easy":
        attempt = 10
    elif difficulty == "hard":
        attempt = 5
    else:
        return "Invalid Difficulty."
    return attempt

def lose_msg():
    print("You are running out of guesses, you lose.")

def new_round_msg():
    while True:
        choice = input("Type 'y' for new round or 'n' for quit: ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid choice. Please type again.")

def end_msg():
    print("Good Bye.")

def game_logic(attempt, answer):
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print("Boom. You correctly hit the answer!")
            return
        elif 0 < guess < answer:
            print("Too low.\nGuess again.")
            attempt -= 1
        elif 100 > guess > answer:
            print("Too high.\nGuess again.")
            attempt -= 1
        else:
            print("Out of range")
    lose_msg()

def number_guessing_game():
    start_new_round = True
    while start_new_round:
        answer = random.randint(1,100)
        difficulty = start_msg(answer)
        attempt = attempt_for_guessing(difficulty)
        game_logic(attempt, answer)
        start_new_round = new_round_msg()
    end_msg()

number_guessing_game()
