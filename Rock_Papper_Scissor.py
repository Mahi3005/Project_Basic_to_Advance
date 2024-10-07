import random

# Define the list of possible choices
choices = ['rock', 'paper', 'scissor']
computer = random.choice(choices)

# Get user input
user_input = input("Enter your choice (rock, paper, or scissor): ").lower()

# Validate user input
if user_input not in choices:
    print("Invalid input. Please choose 'rock', 'paper', or 'scissor'.")
else:
    print(f"Computer chose: {computer}")
    print(f"You chose: {user_input}")

    # Determine the outcome
    if user_input == computer:
        print("It's a tie!")
    elif (user_input == 'rock' and computer == 'scissor') or \
         (user_input == 'paper' and computer == 'rock') or \
         (user_input == 'scissor' and computer == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
