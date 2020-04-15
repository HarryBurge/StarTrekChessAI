'''
Class for pawn, inherits code for Piece
'''

__authour__ = 'Harry Burge'
__date_created__ = '15/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '15/04/2020'


'''
TODO:-



'''

# Imports
import numpy
import piece_super


class Pawn(piece_super.Piece):

    def __init__(self, facing, coords, img_path='tom', value=1, **kwargs):
        '''
        params:-
            facing : [int,int,int] : Vector of direction facing [x,y,z]
            coords : [int,int,int] : Poisition in the grid [x,y,z]
            img_path : str : Path to the image to use for the piece
            value : int : Value assigned to the piece

            **kwargs:-
                team : str : Name of team that the piece is on
        '''
        super().__init__(coords, img_path, value, **kwargs)

        self.facing = facing
        self.moved = False

        self._no_face_moves = []

        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    self._no_face_moves.append([x,y,z])


    def _pos_move_coords(self, coords):
        '''
        params:-
            coords : [int,int,int] : Poisition in the grid [x,y,z]
        returns:-
            [[int,int,int], ...] : All grid poisitions that could be moved to if there 
                                   is actually a poistion or nothing is blocking
        '''
        hypothrtical_moves = []
        
        for i in self._no_face_moves:

            if numpy.dot(self.facing, i) > 0:
                
                hypothrtical_moves.append(numpy.add(coords, i).tolist())

        return hypothrtical_moves


if __name__=='__main__':
    raise RuntimeError('This is a class and cannot be ran')
