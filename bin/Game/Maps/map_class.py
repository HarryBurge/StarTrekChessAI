'''
Map class. Is used to read in map files and be able to control them.
'''

__authour__ = 'Harry Burge'
__date_created__ = '20/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '20/04/2020'


'''
TODO:-
Turn x into an actual object



'''
import importlib

# Code

class Map:

    def __init__(self, path):
        '''
        params:-
            path : str: import path to the map e.g. bin.Game.Maps.default_star_trek_map
        '''
        
        # Import specfifc map
        map_file = importlib.import_module(path)

        self._board = map_file.map_array


    # Getters
    def get_gridpoi(self, x, y, z):
        return self._board[x][y][z]

    def get_board(self):
        return self._board


    # Funcs
    def move_piece(self, x1, y1, z1, x2, y2, z2):
        taken_piece = self._board[x2][y2][z2]
        self._board[x2][y2][z2] = self._board[x1][y1][z1]
        self._board[x1][y1][z1] = 'x'
        return taken_piece


if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')