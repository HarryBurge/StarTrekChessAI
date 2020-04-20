'''
Class for pawn, inherits code for Piece
'''

__authour__ = 'Harry Burge'
__date_created__ = '15/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '20/04/2020'


'''
TODO:-
Create Valid move coords whilst a board is passed
Img_path



'''

# Imports
from bin.Game.Pieces import piece_class


class Pawn(piece_class.Piece):

    def __init__(self, facing, coords, img_path='imgs/', value=10000, team='Netural', **kwargs):
        '''
        params:-
            coords : [int,int,int] : Poisition in the grid [x,y,z]
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece

            **kwargs:-
                team : str : Name of team that the piece is on
        '''
        super().__init__(coords, img_path+team+'-Pawn.png', value, **kwargs)

        self.facing = facing
        self.moved = False


    def _valid_move_coords(self, board):
        pass


if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')
