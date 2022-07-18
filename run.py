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
def player_weapon():
    """
    This function defines the users choice of "the weapon" and
    converts it into lowercase. So regardles what user types, the
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
        print("You entered wrong value, try again. \n")
        player_weapon()
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


# While loop for comparing results
while True:
    print("")
    user_choice = player_weapon()
    cpu_choice = computer_weapon()
    print("")

    if user_choice == "r":
        if cpu_choice == "r":
            print("You chose ROCK! The computer chose ROCK. You TIED!")
        elif cpu_choice == "p":
            print("You chose ROCK! The computer chose PAPER. You LOST!")
            cpu_wins += 1
        elif cpu_choice == "s":
            print("You chose ROCK! The computer chose SCISSORS. You WON!")
            player_wins += 1
    elif user_choice == "p":
        if cpu_choice == "r":
            print("You chose PAPER! The computer chose ROCK. You WON!")
            player_wins += 1
        elif cpu_choice == "p":
            print("You chose PAPER! The computer chose PAPER. You TIED!")
        elif cpu_choice == "s":
            print("You chose PAPER! The computer chose SCISSORS. You LOST!")
            cpu_wins += 1
    elif user_choice == "s":
        if cpu_choice == "r":
            print("You chose SCISSORS! The computer chose ROCK. You LOST!")
            cpu_wins += 1
        elif cpu_choice == "p":
            print("You chose SCISSORS! The computer chose PAPER. You WON!")
            player_wins += 1
        elif cpu_choice == "s":
            print("You chose SCISSORS! The computer chose SCISSORS. You TIED!")
    print("")
    print("Your WINs: " + str(player_wins))
    print("Computer WINs: " + str(cpu_wins))
    print("")

    user_choice = input("Would you like to play again? (Y/N): \n")
    if user_choice in ["Y", "y", "Yes", "yes", "yeah", "yep"]:
        pass
    elif user_choice in ["N", "n", "No", "no"]:
        print("Thank you for playing!")
        print("Have a nice day! \n")
        break
    else:
        break
