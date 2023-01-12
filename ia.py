from random import *

def ia(board, signe):
    symbol_index = None
    opponent_index = None
    if signe == "X":
        symbol_index = 1
        opponent_index = 2
    elif signe == "○":
        symbol_index = 2
        opponent_index = 1
    else:
        return False

    # stores indexes of empty tiles
    empty_tiles = []
    i = 0
    while i < len(board):
        if board[i] == 0:
            empty_tiles += [i]
        i += 1

    if 0 < len(empty_tiles) <= 9:
        i = 0
        for tile in empty_tiles:
            if checkrow(board, tile, symbol_index) or checkcol(board, tile, symbol_index) or checkdiag(board, tile, symbol_index):
                return tile
            if checkrow(board, tile, opponent_index) or checkcol(board, tile, opponent_index) or checkdiag(board, tile, opponent_index):
                return tile

        # random from available tiles
        return empty_tiles[randint(0, len(empty_tiles)-1)]

    return False

def checkrow(board, board_index, player_symbol_index):
    if board_index == 0 or board_index == 3 or board_index == 6:
        if board[board_index + 1] == player_symbol_index and board[board_index + 2] == player_symbol_index:
            return True
    elif board_index == 1 or board_index == 4 or board_index == 7:
        if board[board_index - 1] == player_symbol_index and board[board_index + 1] == player_symbol_index:
            return True
    elif board_index == 2 or board_index == 5 or board_index == 8:
        if board[board_index - 2] == player_symbol_index and board[board_index - 1] == player_symbol_index:
            return True
    return False
def checkcol(board, board_index, player_symbol_index):
    if 0 <= board_index <= 2:
        if board[board_index + 3] == player_symbol_index and board[board_index + 6] == player_symbol_index:
            return True
    elif 3 <= board_index <= 5:
        if board[board_index - 3] == player_symbol_index and board[board_index + 3] == player_symbol_index:
            return True
    elif 6 <= board_index <= 8:
        if board[board_index - 6] == player_symbol_index and board[board_index - 3] == player_symbol_index:
            return True

    return False
def checkdiag(board, board_index, player_symbol_index):
    if board_index == 0:
        if board[4] == player_symbol_index and board[8] == player_symbol_index:
            return True
    elif board_index == 2:
        if board[4] == player_symbol_index and board[6] == player_symbol_index:
            return True
    elif board_index == 4:
        if (board[0] == player_symbol_index and board[8] == player_symbol_index) or (board[2] == player_symbol_index and board[6] == player_symbol_index):
            return True
    elif board_index == 6:
        if board[2] == player_symbol_index and board[4] == player_symbol_index:
            return True
    elif board_index == 8:
        if board[2] == player_symbol_index and board[4] == player_symbol_index:
            return True