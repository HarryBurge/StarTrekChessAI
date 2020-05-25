__authour__ = 'Harry Burge'
__date_created__ = '25/05/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '25/05/2020'

# Imports
import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen

from bin.Utils.game_util import loops
from bin.Visualliser.BoardViews.TwoDViewBoard import TwoDViewBoard
from bin.Visualliser.UIs.AllBoards import AllBoards
from bin.Visualliser.UIs.SwitchBoard import SwitchBoard


# Visualliser
class Visualliser(App):
    '''
    A class that uses kivy to display chess boards to it. Can handle multiple.
    '''

    def __init__(self, game_controllers, option_style='2dviewVertical-switchboardVertical',
                BCKGRND_CLR=[1,1,1,0.1], WHITE_FREE=[1,1,1,0.6], BLACK_FREE=[1,1,1,0.4],
                *args, **kwargs):
        '''
        params:-
            game_controllers : (Game_Controller, ...) : keeps link to the gamecontroller that controls this
            option_style : str : Option of what visualliser style you want
            BCKGRND_CLR : [int,int,int,int] : Colour of the background
            WHITE_FREE : [int,int,int,int] : Mask to put over BCKGRND_CLR on white tiles
            BLACK_FREE : [int,int,int,int] : Mask to put over BCKGRND_CLR on black tiles
        '''
        super().__init__(*args, **kwargs)

        self.game_controllers = game_controllers
        self.option_style = option_style
        self.style = {'background':BCKGRND_CLR, 'whitetile':WHITE_FREE, 'blacktile':BLACK_FREE}


    def build(self):
        '''
        params:-
            None
        returns:-
            GridLayout : Builds visuals to be displayed when app.run()
        '''

        screens = []
        self.boards = []

        if self.option_style.split('-')[0] == '2dviewVertical':

            # Create a board view for all games passed
            for index, game_controller in enumerate(self.game_controllers):
                screen = Screen(name=str(index))
                board = TwoDViewBoard(self, game_controller)

                self.boards.append(board)
                screen.add_widget(board)

                screens.append(screen)

        if self.option_style.split('-')[1] == 'switchboardVertical':
            # Add switchable ui
            self.visual = SwitchBoard(self, screens)

        elif self.option_style.split('-')[1] == 'allVertical':
            # Store screens in columns
            self.visual = AllBoards(self, screens)


        self.visual.height = 100

        return self.visual

    
    def update_board(self, game_controller, board_map):
        '''
        params:-
            game_controller : GameController : The gamecontroller of the 
                                                board you want to update
            board_map : Map : Map of what you want to show visuals
        returns:-
            None : However updates the kivy window
        '''
        for board in self.boards:
            if board.game_controller == game_controller:
                board.update_board(board_map)
