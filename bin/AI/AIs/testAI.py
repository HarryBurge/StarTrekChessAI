__authour__ = 'Harry Burge'
__date_created__ = '20/06/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '20/06/2020'

# Imports
from bin.AI.ai_class import AI
from random import randint
from bin.Utils.game_util import normalise
from bin.Game.Pieces.StarTrekChess.pawn_s import Pawn
import copy

'''
Simulate every move the AI could make - Make sure to be threaded
Check a few of the values calculated with diffrent weighting to make like an A*
search algorithm
Will need to covert values from AI to be able to be smaller the better for the heuristic to work on a*
This is due to it be shortest path

some times on visualliser a peice doesn't change
'''

class Bot(AI):

    def __init__(self):
        super().__init__()


    def suggest_move(self, board, team):

        view = [] # Heuristic value, moves to get to the state, depth

        for heuristic, move in self.calculate_best_moves(board, team, 4):
            view.append((heuristic, [move], 0))

        yn = True
        while yn:
            print('Thinking')

            # Finds the moveset we will be investigating
            min_index = self.minimumn_heurstic_index(view)
            cur_min_heuristic, cur_min_moves, cur_min_depth = view[min_index]

            if cur_min_depth >= 1:
                yn = False
            else:
                # Gets board to current state of the move set found
                simulated_board = copy.deepcopy(board)
                for coords1, coords2 in cur_min_moves:
                    simulated_board.move_piece(*coords1, *coords2)

                # Need to delete old thing from the view
                del view[min_index]

                # Go through the calcualted thing and put into view carrying on the data from prevoius generation
                for heuristic, move in self.calculate_best_moves(simulated_board, team, 4):
                    view.append((cur_min_heuristic+heuristic, cur_min_moves+[move], cur_min_depth+1))

        # Finds the moveset we will be investigating
        min_index = self.minimumn_heurstic_index(view)
        cur_min_heuristic, cur_min_moves, cur_min_depth = view[min_index]

        return cur_min_moves[0][0], cur_min_moves[0][1]
        


    def minimumn_heurstic_index(self, view):
        minh = 100000
        mini = None

        for index, i in enumerate(view):
            if i[0] < minh:
                mini = index
                minh = i[0]

        return mini

    
    def calculate_best_moves(self, board, team, width):
        top_heuristics = [10]*width
        corresponding_moves = [((0,0,0), (0,0,0))]*width

        # Loop through all possible moves of all teams pieces
        for coord1, piece1 in board.get_pieces_search(True, team):
            for move in piece1.valid_move_coords(board, *coord1):

                if move['mv_type'] in ['Take', 'Move']:
                    heuristic = self.heuristic_value_board_state(self.simulate_piece_move(board, *coord1, *move['coords']), team)

                    if max(top_heuristics) > heuristic:
                        index = top_heuristics.index(max(top_heuristics))
                        top_heuristics[index] = heuristic
                        corresponding_moves[index] = (coord1, move['coords'])
                
        return [(top_heuristics[i], corresponding_moves[i]) for i in range(len(top_heuristics))]


    def heuristic_value_board_state(self, board, team):
        num_unsafe_peices = len(self.get_unsafe_pieces_on_team(board, team))
        num_safe_pieces = len(self.get_safe_pieces_on_team(board, team))
        num_same_row_pawns = self.count_pawns_same_column_on_team(board, team, Pawn)

        num_of_possible_attacks = 0
        for coords, piece in board.get_pieces_search(True, team):
            num_of_possible_attacks += len(self.get_on_piece_attacking_pieces(board, *coords, piece))

        #TODO: Create some for defending and people attacking pieces

        num_of_pieces_on_team = len(board.get_pieces_search(True, team))
        num_of_pieces_off_team = len(board.get_pieces_search(False, team))
        num_of_pawns_on_team = len(board.get_pieces_search(True, team, Pawn))

        inv_num_unsafe_peices = num_of_pieces_on_team - num_unsafe_peices
        inv_num_same_row_pawns = num_of_pawns_on_team - num_same_row_pawns
        inv_num_of_possible_attacks = num_of_pieces_off_team - num_of_possible_attacks

        nor_inv_num_unsafe_peices = normalise(inv_num_unsafe_peices, num_of_pieces_on_team, 0)
        nor_num_safe_pieces = normalise(num_safe_pieces, num_of_pieces_on_team, 0)
        nor_inv_num_same_row_pawns = normalise(inv_num_same_row_pawns, num_of_pawns_on_team, 0)
        nor_inv_num_of_possible_attacks = normalise(inv_num_of_possible_attacks, num_of_pieces_off_team, 0)

        vals = [nor_inv_num_unsafe_peices, nor_num_safe_pieces, nor_inv_num_same_row_pawns, nor_inv_num_of_possible_attacks]
        weights = [1,1,1,1]

        sum_valxweight = 0

        for i in range(len(vals)):
            sum_valxweight += vals[i]*weights[i]

        return sum_valxweight

    def get_unsafe_pieces_on_team(self, board, team):
        unsafe_pieces = []

        for coords1, piece1 in board.get_pieces_search(True, team):

            unsafe = False

            for coords2, piece2 in board.get_pieces_search(False, team):

                if {'coords':coords1, 'mv_type':'Take'} in piece2.valid_move_coords(board, *coords2):
                    unsafe = True

            if unsafe:
                unsafe_pieces.append((coords1, piece1))

        return unsafe_pieces


    def get_safe_pieces_on_team(self, board, team):
        unsafe_pieces = self.get_unsafe_pieces_on_team(board, team)
        team_pieces = board.get_pieces_search(True, team)

        safe_pieces = [piece for piece in team_pieces if piece not in unsafe_pieces]
        
        return safe_pieces


    def count_pawns_same_column_on_team(self, board, team, pawn_class):
        count = 0
        pawns = board.get_pieces_search(True, team, pawn_class)

        for coords1, peice1 in pawns:

            found = False

            for coords2, peice2 in pawns:
                if coords2 != coords1 and coords1[0] == coords2[0]: found = True

            if found: count += 1
        
        return count


    def get_attacking_pieces_on_piece(self, board, x,y,z, on_piece):
        attacking_pieces = []

        # All other team pieces
        team_pieces = board.get_pieces_search(True, on_piece.team)
        all_pieces = board.get_all_pieces()
        other_teams_pieces = [i for i in all_pieces if i not in team_pieces]

        for coords, piece in other_teams_pieces:

            valid_moves = piece.valid_move_coords(board, *coords)

            if {'coords':(x,y,z), 'mv_type':'Take'} in valid_moves:
                attacking_pieces.append((coords, piece))

        return attacking_pieces


    def get_on_piece_attacking_pieces(self, board, x,y,z, on_piece):
        potential_attacks = []

        valid_moves = on_piece.valid_move_coords(board, x,y,z)
        for move in valid_moves:
            if move['mv_type'] == 'Take':
                potential_attacks.append((move['coords'], board.get_gridpoi(*move['coords'])))

        return potential_attacks


    def simulate_piece_move(self, board, x1,y1,z1, x2,y2,z2):
        simulated_board = copy.deepcopy(board)
        if simulated_board.move_piece(x1,y1,z1, x2,y2,z2) == False:
            return False
        return simulated_board