__authour__ = 'Harry Burge'
__date_created__ = '20/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '18/05/2020'

# Imports
import importlib
import copy
from bin.Game.piece_class import Piece


# Map
class Map:
    '''
    Used to read a board/map, into a usable class.
    
    Info:-
        -Map file that is pointed to by path needs to have
        map_array = <array>
        -'@' Means a board poistion that any piece can enter
        -'x' Means it is outside the board and no pieces can enter
        -map_array needs to be 3D so [[[], ...], ...]
        -map_array has to have consistent size just fill up with 'x's if needed
    '''

    def __init__(self, path):
        '''
        params:-
            path : str: Import path to the map e.g. 
                bin.Game.Maps.default_star_trek_map
        '''
        # Import map file, based on path given
        map_file = importlib.import_module(path)

        self._board = map_file.map_array

        # Size of (x,y,z)
        self._size = (len(self._board[0][0]), 
                            len(self._board[0]), 
                            len(self._board))


    # Getters
    def get_gridpoi(self, x, y, z):
        '''
        params:-
            x,y,z : int : Coordinates of what you want to return
        returns:-
            False|Piece_subclass|str : False if coordinates are out 
                of range else returns the Piece or string in that 
                coords of the boord
        '''
        # Python excepts negative numbers which we don't want
        if x < 0 or y < 0 or z < 0:
            return False
        else:
            try:
                return self._board[z][y][x]
            except IndexError:
                return False


    def get_all_pieces(self):
        '''
        params:-
            None
        returns:-
            [((int,int,int), Piece_subclass), ...] : Searchs entire board
                and returns the coordinates and piece object of the piece found 
        '''
        all_pieces = []

        for z in range(self._size[2]):
            for y in range(self._size[1]):
                for x in range(self._size[0]):

                    # Check if at x,y,z in board it is a subclass of Piece
                    if issubclass(type(self.get_gridpoi(x,y,z)), Piece):
                        all_pieces.append( ((x,y,z), self.get_gridpoi(x,y,z)) )

        return all_pieces


    def _get_board_array(self):
        '''
        params:-
            None
        returns:-
            [[[str|Piece_subclass, ...], ...], ...] : The entire board
        '''
        return self._board

    
    # Setters
    def _set_gridpoi(self, x,y,z, piece):
        '''
        params:-
            x,y,z : int : Coords to be replaced
            piece : str|Piece_subclass|List : List is only really used for 
                visualiser
        returns:-
            None|False : False if the coords are wrong, else None
        '''
        # Python excepts negative numbers which we don't want
        if x < 0 or y < 0 or z < 0:
            return False
        else:
            try:
                self._board[z][y][x] = piece
            except IndexError:
                return False


    # Funcs
    def move_piece(self, x1, y1, z1, x2, y2, z2):
        '''
        params:-
            x1,y1,z1 : int : coords of piece to move
            x2,y2,z2 : int : coords of where to move to
        returns:-
            False|str|Piece_subclass : False if coords are wrong
                else whatever has been removed from the board
        '''
        # Python excepts negative numbers which we don't want
        if x1 < 0 or y1 < 0 or z1 < 0 or x2 < 0 or y2 < 0 or z2 < 0:
            return False

        # Make sure both coords are correct
        elif self.get_gridpoi(x1,y1,z1) == False or self.get_gridpoi(x2,y2,z2) == False:
            return False

        else:
            
            taken_piece = self.get_gridpoi(x2,y2,z2)

            # Move coords1 to coords 2
            self._set_gridpoi(x2,y2,z2, self.get_gridpoi(x1,y1,z1))

            # Make coords 1 a free space
            self._set_gridpoi(x1,y1,z1, '@')

            return taken_piece

    
    def is_in_check(self, team, king_class):
        '''
        params:-
            team : str : Team of the king you want to see if in check e.g. White
            king_class : Class : The class of king
        returns:-
            bool : True if in check else False
        '''
        kings_coords = []
        other_teams_validmoves = []

        # Search for kings of right team
        for coords, piece in self.get_all_pieces():

            if type(piece) == king_class and piece.team == team:
                kings_coords.append(coords)

            # Due to kings needing to simulate check in valid_move_coords will create a
            # recursion error therefore a none check tested valid move coords need to be used
            elif type(piece) == king_class and piece.team != team:
                        
                for i in piece.valid_move_coords_untested(self, *coords):
                    other_teams_validmoves.append(i['coords'])

            # Collects all other teams valid moves
            elif issubclass(type(piece), Piece) and piece.team != team:
                
                for i in piece.valid_move_coords(self, *coords):
                    other_teams_validmoves.append(i['coords'])

        # If any king is in a valid move of another enemy unit it is in check
        for coords in kings_coords:
            if coords in other_teams_validmoves:
                return True

        return False


    def is_in_checkmate(self, team, king_class):
        '''
        params:-
            team : str : Team of the king you want to see if in check e.g. White
            king_class : Class : The class of king
        returns:-
            bool : True if in checkmate else False
        '''
        # Checks whether king is in check currently
        if self.is_in_check(team, king_class) == False:
            return False

        kings_coords = []
        teams_moves = []

        # Search for kings of right team
        for coords, piece in self.get_all_pieces():

            # If king and right team then record where it is and the object itself
            if type(piece) == king_class and piece.team == team:
                kings_coords.append((coords, piece))

            # Record all valid moves of same team
            elif issubclass(type(piece), Piece) and piece.team == team:
                
                for i in piece.valid_move_coords(self, *coords):
                    teams_moves.append((coords, i['coords']))
                    

        for coords, king in kings_coords:

            # If king can actually move somewhere
            if king.valid_move_coords(self, *coords) != []:
                return False

            # Does any other move team can make stop the check
            for p1,p2 in teams_moves:

                simulated_board = copy.deepcopy(self)
                simulated_board.move_piece(*p1, *p2)

                if simulated_board.is_in_check(team, king_class) == False:
                    return False

        return True


if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')