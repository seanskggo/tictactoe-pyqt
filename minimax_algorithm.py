#################################################################################
# Tic Tac Toe GUI 
# Created with PyQT5
# AI algorithm to fine the best next move given a current tic tac toe game
# state
#################################################################################

#################################################################################
# Globals
#################################################################################

state_count = 0

#################################################################################
# Functions
#################################################################################

def best_move(game_state, player):
    ''' utilises the minimax algorithm to find the best move for bot. 
    Given the current game state and the player whom must make a turn,
    this function returns the index number of the best move
    ''' 
    global state_count
    best_value, best_index = (-1 if player else 1), None
    for index, spot in enumerate(game_state):
        if spot is None:
            state_count += 1
            # For each empty spot. check if the state is optimal
            copy_state = game_state.copy()
            copy_state[index] = player
            value = minimax(copy_state, (not player))
            if value < best_value and (not player):
                best_value, best_index = value, index
            elif value > best_value and player:
                best_value, best_index = value, index
    print(f"Calculated {state_count} possibilites in this move")
    state_count = 0
    return best_index

def minimax(game_state, is_maximising):
    ''' Deploys minimax algorithm. Returns 1 if the game state is winning,
    -1 if losing or 0 if drawing
    ''' 
    global state_count
    state_count += 1
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
                state_count += 1
                copy_state = game_state.copy()
                copy_state[index] = is_maximising
                value = minimax(copy_state, (not is_maximising))
                best_value = max(best_value, value)
    # If minimiser's move:
    else:  
        best_value = 1
        for index, spot in enumerate(game_state):
            if spot is None:
                state_count += 1
                copy_state = game_state.copy()
                copy_state[index] = is_maximising
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
