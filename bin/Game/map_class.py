__authour__ = 'Harry Burge'
__date_created__ = '20/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '18/05/2020'

# Imports
import importlib
import copy

from bin.Game.piece_class import Piece
from bin.Utils.game_util import loops
from bin.Game.attack_board_class import AttackBoard


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
        self._attackmap = map_file.attack_boards_array

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

    
    def get_attack_gridpoi(self, ax, ay):
        '''
        params:-

        returns:-
        '''
        # Python excepts negative numbers which we don't want
        if ax < 0 or ay < 0:
            return False
        else:
            try:
                return self._attackmap[ay][ax]
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

        for x,y,z in loops(range(self._size[0]), range(self._size[1]), range(self._size[2])):

            # Check if at x,y,z in board it is a subclass of Piece
            if issubclass(type(self.get_gridpoi(x,y,z)), Piece):
                all_pieces.append( ((x,y,z), self.get_gridpoi(x,y,z)) )

        return all_pieces

    
    def get_pieces_of_team(self, team):
        '''
        params:-
            team : str : Team to look for peices
        returns:-
            [((int,int,int), Piece_subclass), ...] : Searchs entire board
                and returns the coordinates and piece object of the piece found 
        '''
        team_pieces = []

        for x,y,z in loops(range(self._size[0]), range(self._size[1]), range(self._size[2])):

            # Check if at x,y,z in board it is a subclass of Piece and part of team
            if issubclass(type(self.get_gridpoi(x,y,z)), Piece) and self.get_gridpoi(x,y,z).team == team:
                team_pieces.append( ((x,y,z), self.get_gridpoi(x,y,z)) )

        return team_pieces


    def _get_board_array(self):
        '''
        params:-
            None
        returns:-
            [[[str|Piece_subclass, ...], ...], ...] : The entire board
        '''
        return self._board


    def _get_attack_board_array(self):
        return self._attackmap

    
    # Setters
    def set_gridpoi(self, x,y,z, piece):
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

    
    def set_attack_gridpoi(self, ax, ay, board):
        # Python excepts negative numbers which we don't want
        if ax < 0 or ay < 0:
            return False
        else:
            try:
                self._attackmap[ay][ax] = board
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
            self.set_gridpoi(x2,y2,z2, self.get_gridpoi(x1,y1,z1))

            # Make coords 1 a free space
            self.set_gridpoi(x1,y1,z1, '@')

            return taken_piece


    def move_attack_board(self, ax1, ay1, ax2, ay2):

        if ax1 < 0 or ay1 < 0 or ax2 < 0 or ay2 < 0:
            return False

        elif self.get_attack_gridpoi(ax1, ay1) == False or self.get_attack_gridpoi(ax2, ay2) == False:
            return False

        elif not(type(self.get_attack_gridpoi(ax1, ay1)) == AttackBoard and type(self.get_attack_gridpoi(ax2, ay2)) == tuple):
            return False

        else:
            # Gets actual board coords
            x1,y1,z1 = self.get_attack_gridpoi(ax1, ay1).get_coords()
            x2,y2,z2 = self.get_attack_gridpoi(ax2, ay2)

            # Moves board in attack map
            self.set_attack_gridpoi(ax2, ay2, self.get_attack_gridpoi(ax1, ay1))
            self.get_attack_gridpoi(ax2, ay2).set_coords(x2,y2,z2)
            self.set_attack_gridpoi(ax1, ay1, (x1,y1,z1))

            # Moves x1,y1,z1 to x2,y2,z2 factoring in the area of attack board
            for dx,dy,dz in self.get_attack_gridpoi(ax2, ay2).get_diffrence_area_coords():
                self.set_gridpoi(x2+dx, y2+dy, z2+dz, self.get_gridpoi(x1+dx, y1+dy, z1+dz))
                self.set_gridpoi(x1+dx, y1+dy, z1+dz, 'x')

    
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