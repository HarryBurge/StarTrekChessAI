__authour__ = 'Harry Burge'
__date_created__ = '16/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '19/05/2020'

# Imports
from bin.Game import piece_class
from bin.Utils.game_util import loops


class Bishop(piece_class.Piece):
    '''
    Class for bishop, inherits code for Piece
    '''

    def __init__(self, img_path='bin/Game/Pieces/imgs/', value=3, team='Netural'):
        '''
        params:-
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece
            team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-Bishop.png', value, team)


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

        for dx,dy,dz in loops([-1,1], [-1,1], range(-1,2)):
                        
            for i in self.rec_line_StarTrek(board, x+dx, y+dy, z+dz, dx,dy):
                if not(i in valid_moves):
                    valid_moves.append(i)

        return valid_moves



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')