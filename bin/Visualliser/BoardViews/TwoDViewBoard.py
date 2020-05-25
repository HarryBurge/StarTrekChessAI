__authour__ = 'Harry Burge'
__date_created__ = '25/05/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '25/05/2020'

# Imports
from kivy.uix.gridlayout import GridLayout
from bin.Utils.game_util import loops
from bin.Visualliser.Tiles import BackgroundColor, Square


# TwoDViewBoard
class TwoDViewBoard(GridLayout):
    '''
    Holds a grid layout of tiles of a board in a fully 2D view even if board is 3D
    '''

    def __init__(self, app, game_controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        params:-
            app : Visualliser : Object that has spawned this one
            game_controller : Game assigned to this board
        '''

        self.app = app
        self.game_controller = game_controller

        # will hold all squares created by below function for later callback
        self.squares = []

        board_map = game_controller.get_map()

        # Makes a vertical board
        self.cols = board_map._size[0]
        self.rows = board_map._size[1] * board_map._size[2]

        # Loops through all map coords
        for z,y,x in loops(range(board_map._size[2]), range(board_map._size[1]), range(board_map._size[0])):

            minimis = False
            
            try:
                # Used to get rid of useless lines in the map to make it look a bit cleaner
                if board_map._get_board_array()[z][y] == ['x'] * board_map._size[0] and board_map._get_board_array()[z][y+1] == ['x'] * board_map._size[0]:
                    minimis = True
            except IndexError:
                pass

            if not minimis:
                current = board_map.get_gridpoi(x,y,z)

                if current == 'x':
                    temp = BackgroundColor(background_color=app.style['background'])

                else:
                    temp = Square(app, game_controller, x,y,z)
                    temp.update_square(x,y,z, current)
                    self.squares.append(temp)

                self.add_widget(temp)
        

    def update_board(self, board_map):
        '''
        params:-
            board_map : Map : Map of which is respect to
        returns:-
            None
        '''
        # For all squares update them based on new map
        for square in self.squares:

            current = board_map.get_gridpoi(square.gx, square.gy, square.gz)
            square.update_square(square.gx, square.gy, square.gz, current)