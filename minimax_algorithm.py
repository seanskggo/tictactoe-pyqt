#################################################################################
# Tic Tac Toe GUI 
# Created with PyQT5
# AI algorithm to fine the best next move given a current tic tac toe game
# state
#################################################################################

#################################################################################
# Functions
#################################################################################

def best_move(game_state, player):
    ''' utilises the minimax algorithm to find the best move for bot. 
    This function returns the index number of the square to be played
    after calculating the best move
    ''' 
    print("-----------NEW MOVE--------------------")
    best_value, best_index = 1, None
    # Check whose turn it is from game board
    for index, spot in enumerate(game_state):
        if spot is None:
            copy_state = game_state.copy()
            copy_state[index] = player
            value = minimax(copy_state, player)
            print(value)
            print_game(copy_state)
            if value < best_value:
                best_value, best_index = value, index
    return best_index

def minimax(game_state, is_maximising):
    ''' Deploys minimax algorithm. Returns 1 if the game state is winning,
    -1 if losing or 0 if drawing
    ''' 
    # If the game condition has ended, return appropriate value
    result = check_if_end(game_state)
    if result is not None:
        return result
    # Else, recursively loop to find game state value (1,0,-1) for 
    # all possible game states using minimax algorithm
    # If maximiser's move:
    if is_maximising:
        best_value = -1
        for index, spot in enumerate(game_state):
            if spot is None:
                copy_state = game_state.copy()
                copy_state[index] = (not is_maximising)
                value = minimax(copy_state, (not is_maximising))
                best_value = max(best_value, value)
    # If minimiser's move:
    else:  
        best_value = 1
        for index, spot in enumerate(game_state):
            if spot is None:
                copy_state = game_state.copy()
                copy_state[index] = (not is_maximising)
                value = minimax(copy_state, (not is_maximising))
                best_value = min(best_value, value)
    return best_value

def check_if_end(game_state):
    ''' Checks the game board to see if the position has won, lost, drawn or 
    neither. Returns 1 if won, -1 if lost, 0 if drawn, or None if the game
    has not ended yet (has valid spots left)
    ''' 
    condition = [
        (game_state[0], game_state[1], game_state[2]),
        (game_state[3], game_state[4], game_state[5]),
        (game_state[6], game_state[7], game_state[8]),
        (game_state[0], game_state[3], game_state[6]),
        (game_state[1], game_state[4], game_state[7]),
        (game_state[2], game_state[5], game_state[8]),
        (game_state[0], game_state[4], game_state[8]),
        (game_state[2], game_state[4], game_state[6])
    ]
    # Check using the conditions
    for check in condition:
        if check == (True, True, True):
            return 1
        elif check == (False, False, False):
            return -1
    # If there are no wins/loses after scanning, determine if the 
    # position is a tie or not (incomplete game state)
    if game_state.count(None) == 0:
        return 0
    else: 
        return None











def print_game(yeet):
    game_state = yeet.copy()
    for index, i in enumerate(game_state):
        if i is True:
            game_state[index] = 'O'
        elif i is False:
            game_state[index] = 'X'
        else:
            game_state[index] = ' '
    print("-----------")
    print(" " + " | ".join(game_state[0:3]))
    print("-----------")
    print(" " + " | ".join(game_state[3:6]))
    print("-----------")
    print(" " + " | ".join(game_state[6:9]))
    print("-----------")
    print("")