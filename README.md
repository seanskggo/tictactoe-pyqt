# Tic Tac Toe AI

Tic Tac Toe game GUI: compete against a perfect AI in a match of Tic Tac Toe.\
The algorithm uses the minimax algorithm to check all game states before playing optimum moves. \
Since Tic Tac Toe is a solved game, there is a mathematically proven strategy that will guarantee at least a draw. Hence, this AI will never lose against any opponent.

## Setup

To download all the neccessary python packages to execute (or modify) the program, run

``` pip install -r requirements.txt ```

To run the program, call

``` python tic_tac_toe_gui.py ``` or ``` python3 tic_tac_toe_gui.py ```

from the main repository containing the dependent files. Your server needs to support X11 forwarding. Otherwise, you can install and setup separately.

## Alternative setup with installer for Windows only

For Windows OS, simply double click tic_tac_toe.exe from folder or run from command line. \
Choose a destination path, then the installer will and install the files and dependencies in that path. 

![3](https://user-images.githubusercontent.com/65769889/102011885-3f877800-3d9b-11eb-8236-1abed503805a.PNG)

Once installed, a new folder named "tic_tac" will be created in that path

![5](https://user-images.githubusercontent.com/65769889/102011944-942af300-3d9b-11eb-9b74-9e7332ecdb0c.PNG)

To run the Tic Tac Toe program, double click or execute the tic_tac_toe_gui application/executable

![4](https://user-images.githubusercontent.com/65769889/102011943-93925c80-3d9b-11eb-8269-00c4ce020944.PNG)

## Customisation

You can choose to use different symbols for the "naughts" and "crosses". \
To do this, simply replace the "circle.png" and "cross.png" files with your own. The program will resize the images automatically. \
To change the dimensions of the buttons in the GUI, alter the values in dimensions.csv. 

## About the program

The initial game state is an empty 3x3 board. A player can choose to go first by clicking on any of the 9 empty slots or choose to go second by pressing the 
"make AI move" button. This will generate an optimum move. If either player manages to form a row, column or diagonal of the same symbol, the player wins the game. Otherwise, if the board is filled and neither have won, the game is drawn.

![2](https://user-images.githubusercontent.com/65769889/102011883-3e564b00-3d9b-11eb-8526-f83735c1ab96.PNG)

To reset the game at any point in time, press the "reset" button. To make the optimum move at any time, press the "make AI move" button. If you run the program from the command line, a useful metric that shows how many game state possibilities were calculated is shown per move.

![1](https://user-images.githubusercontent.com/65769889/102011853-1535ba80-3d9b-11eb-8bd9-0b815ea3ecf1.PNG)

