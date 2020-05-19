__authour__ = 'Harry Burge'
__date_created__ = '16/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '19/05/2020'

# Imports
from bin.Game.piece_class import Piece
from bin.Utils.game_util import loops


# Castle
class Castle(Piece):
    '''
    Class for castle, inherits code for Piece
    '''

    def __init__(self, img_path='bin/Game/Pieces/imgs/', value=5, team='Netural'):
        '''
        params:-
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece
            team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-Castle.png', value, team)


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

        for dz, d in loops(range(-1,2), [-1, 1]):

            # Checks along dx
            for i in self.rec_line_StarTrek(board, x+d, y, z+dz, d,0):
                if not(i in valid_moves):
                    valid_moves.append(i)

            # Checks along dy
            for i in self.rec_line_StarTrek(board, x, y+d, z+dz, 0,d):
                if not(i in valid_moves):
                    valid_moves.append(i)

        return valid_moves



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')