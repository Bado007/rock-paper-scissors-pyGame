# Rock Paper Scissors terminal game.

import random 


# define variables for the game 
cpu_wins = 0
player_wins = 0 


def choose_weapon():
    """
    This function defines 
    """
    user_choice = input("Choose Rock, Paper, Scissors: ")
    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "r"

