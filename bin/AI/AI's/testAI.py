__authour__ = 'Harry Burge'
__date_created__ = '20/06/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '20/06/2020'

# Imports
from bin.AI.ai_class import AI
from random import randint


class Bot(AI):

    def __init__(self):
        super().__init__()


    def suggest_move(self, board, team):
        if len(board.get_all_pieces())-1 > 0:
            selected_piece = board.get_all_pieces()[randint(0, len(board.get_all_pieces())-1)]

            if selected_piece[1].team == team:
                coords1 = selected_piece[0]
                valid_moves = selected_piece[1].valid_move_coords(board, *coords1)

                if len(valid_moves)-1 > 0:
                    coords2 = valid_moves[randint(0, len(valid_moves)-1)]['coords']

                    return coords1, coords2

        return False, False