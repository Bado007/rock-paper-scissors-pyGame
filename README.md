# Rock, Paper, Scissors Game

Rock, Paper, Scissors is a Python terminal game which runs in mock terminal on Heroku.

Users can try to win against the computer that chooses their figure completely randomly.

[Here is the LIVE version of the project](https://rock-paper-scissors-pyame.herokuapp.com/)

<img width="1440" alt="Screenshot 2022-07-19 at 23 56 30" src="https://user-images.githubusercontent.com/103571907/179942336-833ba99b-9fdc-4cb0-a05a-a5d8c9d73dc1.png">

## How to play

A simultaneous game, it has three possible outcomes: a win, a loss or a draw. A player who decides to play rock will beat another player who has chosen scissors, but will lose to one who has played paper (paper covers rock); a play of paper will lose to a play of scissors (scissors cuts paper). If both players choose the same shape / figure, the game is tied and is usually immediately replayed to break the tie. 

Rock Paper Scissors is often used as a fair choosing method between two people, similar to throwing dice, in order to settle a dispute or make an unbiased group decision. Unlike traditional game, truly random selection methods, take place in this terminal game. for more information visit [Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors).

## Features 

#### Welcome message
- A welcome message that greets and encourages the user's competitive spirit.

![Namnlös](https://user-images.githubusercontent.com/103571907/179949828-b2150d4d-b252-4c75-aa17-b602985325c9.png)

#### Figure selection 
- The computer randomly selects their figure to compete.
- The user can choose between them by entering their first letter (for example "p" for paper) or enter full word for it.
- User may enter their figure selection in capital letters as well 
- In case of a typo or, choosing a figure that is not defined in the game, it prints the message encouraging the user of trying again. 

![2](https://user-images.githubusercontent.com/103571907/179949792-4fc85f01-9e2a-4f17-a392-e3e6c025b3ec.png)

#### Score counting 
- Description on which figures were used by the computer and the user.
- The game counts scores and assigns them to the winner.

 ![score](https://user-images.githubusercontent.com/103571907/179950613-b2f19425-6ed4-4fde-8dce-4797fe456480.png)
 
 #### Play again message
 - Encouraging user to continue playing the game.
 - Selection input YES and NO (the game recognizes small, capital or first letters) 
 
![again](https://user-images.githubusercontent.com/103571907/179951473-f49f5ba9-c030-4399-a35b-c1cc1967eb5e.png)

#### Goodbye greeting 
- Polite attitude to greet user when leaving.
- Giving a positive user experience.

![thanks](https://user-images.githubusercontent.com/103571907/179952047-d0e83d41-a966-4091-8923-e34f158550c8.png)

#### User inputs
- User inputs, always on a new line.
- Looks better on the eye and gives a positive user experience.

## Testing 

I have manually tested the code by doing the following:

- Passed the code through [PEP8](http://pep8online.com/) validator and confirmed no problems.
- Assign additional strings for user inputs, for example (NO as nope) to eliminate typing Errors.
- Tested in my local terminal and also in Heroku terminal.

## Bugs 

During the coding, I encountered few bugs:

- Inputs were not recognized / defined and program did not execute code till the end.
- Score counting 

Solved Bugs:
- Add additional strings as input options, in order, if user decides to use "slang" words for YES and NO.
- Assign score counting variables as strings.

Remaining Bugs:
- There are no remaining bugs.
- Code passed [PEP8](http://pep8online.com/) validation.

## Deployment

This project used Code Institute's mock terminal for [Heroku](https://www.heroku.com/home) terminal.

Steps for deployment:


