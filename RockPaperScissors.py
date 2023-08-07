import random

# getting input from user
def get_user_choice():
    choice = input("Choose rock (r), paper (p), or scissors (s): ")
    if choice in ['r', 'p', 's']:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()
    
# generating choice of computer
def get_computer_choice():
    choices = ['r', 'p', 's']
    return random.choice(choices)

# determining winner by comparing
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        return "You win!"
    else:
        return "Computer wins!"
    
# asking user to play again
def play_again():
    choice = input("Do you want to play again? (y/n): ")
    return choice.lower()

# main function
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        if play_again() != "y":
            break
        

print("Let's play Rock, Paper, Scissors!")
play_game()
