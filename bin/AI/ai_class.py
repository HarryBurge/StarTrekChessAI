__authour__ = 'Harry Burge'
__date_created__ = '20/06/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '20/06/2020'

import copy
import numpy as np
import tensorflow as tf


class AI:

    def __init__(self):
        pass


    def suggest_move(self, board, team, all_teams):
        pass

    def simulate_piece_move(self, board, x1,y1,z1, x2,y2,z2):
        simulated_board = copy.deepcopy(board)
        if simulated_board.move_piece(x1,y1,z1, x2,y2,z2) == False:
            return False
        return simulated_board

    def convert_map_to_float_vector(self, board, team):
        board_array = board._get_board_array()
        
        for coord, piece in board.get_pieces_search(True, team=team):
            board_array[coord[2]][coord[1]][coord[0]] = piece.value

        for coord, piece in board.get_pieces_search(False, team=team):
            board_array[coord[2]][coord[1]][coord[0]] = -piece.value

        for z in range(len(board_array)):
            for y in range(len(board_array[z])):
                for x in range(len(board_array[z][y])):
                    if board_array[z][y][x] == 'x':
                        board_array[z][y][x] = 0
                    elif board_array[z][y][x] == '@':
                        board_array[z][y][x] = 0.5

        b = np.asarray(board_array, dtype = float)
        b = b.flatten()
        return b

    