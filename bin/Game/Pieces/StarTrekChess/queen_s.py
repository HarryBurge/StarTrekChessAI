__authour__ = 'Harry Burge'
__date_created__ = '16/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '19/05/2020'

# Imports
from bin.Game.piece_class import Piece
from bin.Utils.game_util import loops

# Queen
class Queen(Piece):
    '''
    Class for queen, inherits code for Piece
    '''

    def __init__(self, img_path='bin/Game/Pieces/imgs/', value=9, team='Netural'):
        '''
        params:-
            img_path : str : Path to the folder where images are stores
            value : int : Value assigned to the piece
            team : str : Name of team that the piece is on
        '''
        super().__init__(img_path+team+'-Queen.png', value, team)


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

        for dx,dy,dz in loops(range(-1,2),range(-1,2),range(-1,2)):

            # Can't test along line of dx, dy == 0 because thats a point
            if not(dx==0 and dy==0):
                
                # Due to being StarTrek movement repeats can come from this func
                # so needs to be filtered
                for i in self.rec_line_StarTrek(board, x+dx, y+dy, z+dz, dx,dy):
                    if not(i in valid_moves):
                        valid_moves.append(i)

        return valid_moves



if __name__=='__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')