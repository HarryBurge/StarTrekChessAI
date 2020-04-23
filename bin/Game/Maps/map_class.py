'''
Map class. Is used to read in map files and be able to control them.
'''

__authour__ = 'Harry Burge'
__date_created__ = '20/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '22/04/2020'


'''
TODO:-

'''

# Imports
import importlib


class Map:

    def __init__(self, path):
        '''
        params:-
            path : str: import path to the map e.g. bin.Game.Maps.default_star_trek_map
        '''
        
        # Import specfifc map
        map_file = importlib.import_module(path)

        self._board = map_file.map_array
        self._size = map_file.map_size


    # Getters
    def get_gridpoi(self, x, y, z):
        if x < 0 or y < 0 or z < 0:
            return False
        else:
            try:
                return self._board[z][y][x]
            except IndexError:
                return False

    def get_board(self):
        return self._board


    # Funcs
    def move_piece(self, x1, y1, z1, x2, y2, z2):
        if x1 < 0 or y1 < 0 or z1 < 0 or x2 < 0 or y2 < 0 or z2 < 0:
            return False
        else:
            try:
                taken_piece = self._board[z2][y2][x2]
                self._board[z2][y2][x2] = self._board[z1][y1][x1]
                self._board[z1][y1][x1] = '@'
                return taken_piece
            except IndexError:
                return False



if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')