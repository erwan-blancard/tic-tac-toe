from ia import ia
from random import *

symbols = "X○"
DRAW = 0
P1_VICTORY = 1
P2_VICTORY = 2

def startgame():
    board = [0] * 9
    current_turn = 0
    end_type = 0
    finished = False

    isAI_input = input("Voulez vous jouer contre l'IA ? (O/N) ")
    isAI = isAI_input.lower() == "y" or isAI_input.lower() == "o"
    if isAI:
        # selects who plays first if an AI plays
        AI_turn_index = randint(0, 1)

    while not finished:
        drawboard(board)

        if isAI and (current_turn % 2) == AI_turn_index:
            print("Au JOUEUR", (current_turn % 2) + 1, "(IA) de jouer !")
            AI_input = ia(board, symbols[current_turn % 2])
            # if an error is thrown by function (returns False), exit with error code 1
            if type(AI_input) == bool:
                print("L'IA n'est pas parvenue à jouer pour ce tour...")
                exit(1)
            else:
                board[AI_input] = (current_turn % 2) + 1
        else:
            print("Au JOUEUR", (current_turn % 2) + 1, "de jouer !")
            print("Entrez le numéro de la case où vous souhaitez jouer:", end=" ")
            input_satisfying = False
            while not input_satisfying:
                player_input = input()

                # checks if player_input can be converted to an integer, and if not loops back to input()
                try:
                    player_input = int(player_input)
                except:
                    print("Entrée invalide ! Entrez le numéro de la case où vous souhaitez jouer:", end=" ")
                    continue

                if is_input_satisfying(board, player_input):
                    # fills the corresponding tile
                    board[player_input - 1] = (current_turn % 2) + 1
                    input_satisfying = True
                else:
                    print("Case invalide ! Entrez le numéro de la case où vous souhaitez jouer:", end=" ")

        current_turn += 1
        if current_turn > 4:
            if is_board_filled(board):
                finished = True
                if P1_wins(board):
                    end_type = P1_VICTORY
                elif P2_wins(board):
                    end_type = P2_VICTORY
                else:
                    end_type = DRAW
            else:
                if P1_wins(board):
                    end_type = P1_VICTORY
                    finished = True
                elif P2_wins(board):
                    end_type = P2_VICTORY
                    finished = True

    drawboard(board)
    if end_type == 1:
        print("Bravo ! Le JOUEUR 1 a gagné !")
    elif end_type == 2:
        print("Bravo ! Le JOUEUR 2 a gagné !")
    else:
        print("Égalité ! Aucun joueur n'a gagné !")


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
    return False

def P1_wins(board):
    i = 0
    while i < len(board):
        if board[i] == 1:
            if checkrow(board, i, 1):
                return True
            if checkcol(board, i, 1):
                return True
            if checkdiag(board, i, 1):
                return True
        i += 1
    return False

def P2_wins(board):
    i = 0
    while i < len(board):
        if board[i] == 2:
            if checkrow(board, i, 2):
                return True
            if checkcol(board, i, 2):
                return True
            if checkdiag(board, i, 2):
                return True
        i += 1
    return False

def is_input_satisfying(board, player_input):
    if player_input > len(board) > 0:
        return False
    # checks if given tile is empty
    if board[player_input - 1] == 0:
        return True
    return False
def is_board_filled(board):
    empty_tile_count = 0
    for i in board:
        if i == 0:
            empty_tile_count += 1
    if empty_tile_count == 0:
        return True
    return False
def get_tile(board, x, y):
    return board[x + (y*3)]
def drawboard(board):
    for h in range(3):
        for w in range(3):
            if get_tile(board, w, h) != 0:
                tilesymbol = symbols[get_tile(board, w, h) -1]
            else:
                tilesymbol = str(w + (h*3) + 1)

            print(" ", end="")
            print(tilesymbol[0], end=" ")
        # jump
        print()

startgame()