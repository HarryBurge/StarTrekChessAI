'''
Class for castle, inherits code for Piece
'''

__authour__ = 'Harry Burge'
__date_created__ = '16/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '23/04/2020'


'''
TODO:-
Img_path
Add in castling

'''

# Imports
from bin.Game.Pieces import piece_class


class Castle(piece_class.Piece):

    def __init__(self, img_path='bin/Game/Pieces/imgs/', value=5, team='Netural', **kwargs):
        '''
        params:-
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece

            **kwargs:-
                team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-Castle.png', value, team, **kwargs)

        self.moved = False


    def valid_move_coords(self, board, x,y,z):
        '''
        params:-
            board : Map : Board with respect to
            x,y,z : int : Coords of piece
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of 
                all moves that can be made from this piece
        '''
        valid_moves = []

        for d in [-1, 1]:

            valid_moves += self._rec_line_3D(board, x+d, y, z, d,0,0)
            valid_moves += self._rec_line_3D(board, x, y+d, z, 0,d,0)
            valid_moves += self._rec_line_3D(board, x, y, z+d, 0,0,d)

        return valid_moves



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')