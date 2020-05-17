'''
Class for knight, inherits code for Piece
'''

__authour__ = 'Harry Burge'
__date_created__ = '16/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '23/04/2020'

'''
TODO:-
Img_path

'''

# Imports
from bin.Game.Pieces import piece_class


class Knight(piece_class.Piece):

    def __init__(self, img_path='bin/Game/Pieces/imgs/', value=3, team='Netural', **kwargs):
        '''
        params:-
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece

            **kwargs:-
                team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-Knight.png', value, team, **kwargs)


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

        for dx in [-2, 2]:
            for dy, dz in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                testable_moves.append([x+dx,y+dy,z+dz])

        for dy in [-2, 2]:
            for dx, dz in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                testable_moves.append([x+dx,y+dy,z+dz])

        for dz in [-2, 2]:
            for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                testable_moves.append([x+dx,y+dy,z+dz])

        return self._test_coords(board, testable_moves)



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')