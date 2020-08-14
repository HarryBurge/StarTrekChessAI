__authour__ = 'Harry Burge'
__date_created__ = '16/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '19/05/2020'

# Imports
from bin.Game.piece_class import Piece
from bin.Utils.game_util import loops


# Knight
class Knight(Piece):
    '''
    Class for knight, inherits code for Piece
    '''

    def __init__(self, img_path='bin/Game/Pieces/imgs/', value=3, team='Netural'):
        '''
        params:-
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece
            team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-Knight.png', value, team)


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

        # Creates all moves that horse could create on x axis

        for dx, dy, dz in loops([-2,2], [-1,1], [-1,0,1]):
            testable_moves.append([x+dx,y+dy,z+dz])

        # Creates all moves that horse could create on y axis
        for dx, dy, dz in loops([-1,1], [-2,2], [-1,0,1]):
            testable_moves.append([x+dx,y+dy,z+dz])

        # Tests all moves
        return self.test_coords(board, testable_moves)



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')