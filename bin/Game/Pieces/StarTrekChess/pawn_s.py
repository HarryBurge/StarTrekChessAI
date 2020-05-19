__authour__ = 'Harry Burge'
__date_created__ = '15/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '19/05/2020'

# Imports
import numpy

from bin.Game.piece_class import Piece
from bin.Utils.game_util import loops


# Pawn
class Pawn(Piece):
    '''
    Class for pawn, inherits code for Piece
    '''

    def __init__(self, facing, img_path='bin/Game/Pieces/imgs/', value=1, team='Netural'):
        '''
        params:-
            facing : (int, int) : Which way the pawn is facing dx,dy
            img_path : str : Path to the folder where images are stored
            value : int : Value assigned to the piece
            team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-Pawn.png', value, team)

        self.facing = facing
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
        moves = []

        for dz in range(-1,2):
            
            # Forward movements
            current = self.test_coord(board, x+self.facing[0],y+self.facing[1],z+dz)

            if current != False and current['mv_type'] == 'Move':
                moves.append(current)

            if self.moved == False:

                current = self.test_coord(board, x+self.facing[0]*2,y+self.facing[1]*2,z+dz)

                if current != False and current['mv_type'] == 'Move':
                    moves.append(current)

            # Taking movements
            for dx, dy in loops(range(-1,2),range(-1,2)):

                # Checks whether diffrence between facing and dx,dy is less than 90 degress
                # And are not equal
                if numpy.dot(self.facing, (dx,dy)) > 0 and (dx,dy) != self.facing:

                    current = self.test_coord(board, x+dx,y+dy,z+dz)

                    if current != False and current['mv_type'] == 'Take':
                        moves.append(current)

        return moves



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')
