__authour__ = 'Harry Burge'
__date_created__ = '16/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '19/05/2020'

# Imports
import copy

from bin.Game.piece_class import Piece
from bin.Utils.game_util import loops


# King
class King(Piece):
    '''
    Class for king, inherits code for Piece
    '''

    def __init__(self, img_path='bin/Game/Pieces/imgs/', value=10000, team='Netural'):
        '''
        params:-
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece
            team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-King.png', value, team)


    def valid_move_coords(self, board, x,y,z):
        '''
        params:-
            board : Map : Board with respect to
            x,y,z : int : Coords of piece
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of 
                all moves that can be made from this piece
        '''
        testable_moves = []

        for dx,dy,dz in loops(range(-1,2),range(-1,2),range(-1,2)):

            if not(dx==0 and dy==0 and dz==0):

                current = self.test_coord(board, x+dx, y+dy, z+dz)

                if current != False and current['mv_type'] != 'Defending':

                    # Simulates map and if in check then not a untested valid move
                    simulated_map = copy.deepcopy(board)
                    simulated_map.move_piece(x, y, z, x+dx, y+dy, z+dz)

                    if not simulated_map.is_in_check(self.team, type(self)):
                        testable_moves.append([x+dx,y+dy,z+dz])

                elif current != False and current['mv_type'] == 'Defending':
                    testable_moves.append([x+dx,y+dy,z+dz])
        
        # Tests all moves
        return self.test_coords(board, testable_moves)


    def valid_move_coords_untested(self, board, x,y,z):
        '''
        params:-
            board : Map : Board with respect to
            x,y,z : int : Coords of piece
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of 
                all moves that can be made from this piece, not tested to
                see if in check after the move. This is needed due to
                a recursion error in is_in_checkmate
        '''
        testable_moves = []

        for dx,dy,dz in loops(range(-1,2),range(-1,2),range(-1,2)):

            if not(dx==0 and dy==0 and dz==0):
                testable_moves.append([x+dx,y+dy,z+dz])
            
        # Tests all moves
        return self.test_coords(board, testable_moves)



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')