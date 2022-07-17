# Rock Paper Scissors terminal game.

import random 


# define variables for the game 
cpu_wins = 0
player_wins = 0 

# Welcome Message

hello_msg_border = "======================================================="
hello_msg_text = "Hello! Welcome to Terminal game ROCK, PAPER, SCISSORS!"
hello_msg_excited = "Are you ready to get started?"
hello_msg_ready = "Because your opponent is already warming up!"


print(hello_msg_border)
print(hello_msg_text)
print(hello_msg_excited)
print(hello_msg_ready)
print(hello_msg_border)


# Player choice function
def choose_weapon():
    """
    This function defines the users choice of "the weapon" and
    converts it into lowercase. So regardles what user types the
    function is going to understand it as the first letter of the
    weapon + in lowercase.
    """
    user_choice = input("Choose Rock, Paper, Scissors: ")
    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "s"
    else:
        print("You entered wrong value, try again.")
        choose_weapon()
    return user_choice

# Computer choice function
def computer_weapon():
    """
    This function defines the computer choice of "the weapon" and
    which is picked randomly.
    """
    # Computer randomly picks a number in range 1-3
    cpu_choice = random.randint(1, 3)
    # Logig to assign value to number computer picks
    if cpu_choice == 1:
        cpu_choice = "r"
    elif cpu_choice == 2:
        cpu_choice = "p"
    else:
        cpu_choice = "s"
    return cpu_choice
