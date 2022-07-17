# Rock Paper Scissors terminal game.

import random 


# define variables for the game 
cpu_wins = 0
player_wins = 0 


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

