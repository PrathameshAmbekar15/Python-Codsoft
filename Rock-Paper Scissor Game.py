import random

def get_computer_choice():
    # Randomly select the computer's choice
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    # Compare user choice and computer choice and determine the winner
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Choose your move: rock, paper, or scissors.")
    print("Enter 'exit' to quit the game.")

    while True:
        # Get user input
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

        if user_choice == "exit":
            print("Thanks for playing! Final scores:")
            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue

        # Get the computer's choice
        computer_choice = get_computer_choice()

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        # Display the choices and result
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1
        
        print(f"Scores - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Final scores:")
            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
