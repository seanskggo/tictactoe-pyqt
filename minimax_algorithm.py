#################################################################################
# Tic Tac Toe GUI 
# Created with PyQT5
# AI algorithm to fine the best next move given a current tic tac toe game
# state
#################################################################################

#################################################################################
# Functions
#################################################################################

def minimax(game_state):
    ''' utilises the minimax algorithm to find the best move for bot. 
    This function returns the index number of the square to be played
    after calculating the best move
    ''' 
    for index, i in enumerate(game_state):
        if i is None:
            return index
    return 0
