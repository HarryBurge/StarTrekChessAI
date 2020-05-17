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
import copy
from bin.Game.Pieces.piece_class import Piece


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

    def set_gridpoi(self, x,y,z, piece):
        self._board[z][y][x] = piece

    
    def is_in_check(self, team, king_class):

        kings_coords = []
        other_teams_coords = []

        for z in range(len(self.get_board())):
            for y in range(len(self.get_board()[0])):
                for x in range(len(self.get_board()[0][0])):

                    current = self.get_gridpoi(x,y,z)

                    if type(current) == king_class and current.team == team:
                        kings_coords.append((x,y,z))

                    elif type(current) == king_class and current.team != team:
                        
                        for i in current.valid_move_coords_untested(self, x,y,z):
                            other_teams_coords.append(i['coords'])

                    elif issubclass(type(current), Piece) and current.team != team:
                        
                        for i in current.valid_move_coords(self, x,y,z):
                            other_teams_coords.append(i['coords'])

        for i in kings_coords:
            if i in other_teams_coords:
                return True
        return False

    def is_in_checkmate(self, team, king_class): #believe to be fine but need to fully test

        # Checks whether king is in check currently
        if self.is_in_check(team, king_class) == False:
            return False

        kings_coords = []
        teams_moves = []

        # Find all kings of colour type and moves that team can do
        for z in range(len(self.get_board())):
            for y in range(len(self.get_board()[0])):
                for x in range(len(self.get_board()[0][0])):

                    current = self.get_gridpoi(x,y,z)

                    if type(current) == king_class and current.team == team:
                        kings_coords.append((x,y,z))

                    elif issubclass(type(current), Piece) and current.team == team:
                        
                        # Gets all moves that non kings on same team can make
                        for i in current.valid_move_coords(self, x,y,z):
                            teams_moves.append(((x,y,z), i['coords']))
        
        #print('\n--moves--\n' + str(teams_moves))
        #input()
                    

        for king in kings_coords:

            #print('\n--king--' + str(king))

            current = self.get_gridpoi(*king)

            valid_moves = current.valid_move_coords(self, *king)
            #print('--king moves--' + str(valid_moves))

            # If king can actually move somewhere
            if valid_moves != []:
                return False


            # Does any other move team can make stop the check
            for p1,p2 in teams_moves:
                #print('checking move--' + str(p1) + '--' + str(p2))

                simulated_board = copy.deepcopy(self)
                simulated_board.move_piece(*p1, *p2)

                if simulated_board.is_in_check(team, king_class) == False:
                    #print('Returned false on check')
                    #input()
                    return False

        #input()
        return True


                





if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')