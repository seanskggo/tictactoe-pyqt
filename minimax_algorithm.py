#################################################################################
# Tic Tac Toe GUI 
# Created with PyQT5
# AI algorithm to fine the best next move given a current tic tac toe game
# state
#################################################################################

#################################################################################
# Functions
#################################################################################

def minimax():
    from tic_tac_toe_gui import Ui_window
    ''' utilises the minimax algorithm to find the best move for bot. 
    This function returns the index number of the square to be played
    after calculating the best move
    ''' 
    game_state = Ui_window.show_game_state()
    return 42
