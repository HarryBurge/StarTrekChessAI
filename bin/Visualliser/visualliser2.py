__authour__ = 'Harry Burge'
__date_created__ = '25/05/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '25/05/2020'

# Imports
import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen

from bin.Utils.game_util import loops
from bin.Visualliser.BoardViews.TwoDViewBoard import TwoDViewBoard, TwoDViewBoardH
from bin.Visualliser.UIs.AllBoards import AllBoards, AllBoardsH
from bin.Visualliser.UIs.SwitchBoard import SwitchBoard

from kivy.clock import Clock
Clock.max_iteration = 100


# Visualliser
class Visualliser(App):
    '''
    A class that uses kivy to display chess boards to it. Can handle multiple.
    '''

    # '2dviewVertical-switchboardVertical'
    def __init__(self, game_controllers, option_style='2dviewHorizontal-switchboardHorizontal',
                BCKGRND_CLR=[1,1,1,0.1], WHITE_FREE=[1,1,1,0.6], BLACK_FREE=[1,1,1,0.4], user_interaction=True,
                *args, **kwargs):
        '''
        params:-
            game_controllers : (Game_Controller, ...) : keeps link to the gamecontroller that controls this
            option_style : str : Option of what visualliser style you want
            BCKGRND_CLR : [int,int,int,int] : Colour of the background
            WHITE_FREE : [int,int,int,int] : Mask to put over BCKGRND_CLR on white tiles
            BLACK_FREE : [int,int,int,int] : Mask to put over BCKGRND_CLR on black tiles
            user_interaction : bool : True if you want the user to be able to interact with the visuals else False
        '''
        super().__init__(*args, **kwargs)

        self.game_controllers = game_controllers
        self.option_style = option_style
        self.style = {'background':BCKGRND_CLR, 'whitetile':WHITE_FREE, 'blacktile':BLACK_FREE}
        self.user_interaction = user_interaction
        self.boards = []


    def build(self):
        '''
        params:-
            None
        returns:-
            GridLayout : Builds visuals to be displayed when app.run()
        '''
        self.screens = []

        if self.option_style.split('-')[0] == '2dviewVertical':

            # Create a board view for all games passed
            for index, game_controller in enumerate(self.game_controllers):
                screen = Screen(name=str(index))
                board = TwoDViewBoard(self, game_controller, self.user_interaction)

                self.boards.append(board)
                screen.add_widget(board)

                self.screens.append(screen)

        elif self.option_style.split('-')[0] == '2dviewHorizontal':
            # Create a board view for all games passed
            for index, game_controller in enumerate(self.game_controllers):
                screen = Screen(name=str(index))
                board = TwoDViewBoardH(self, game_controller, self.user_interaction)

                self.boards.append(board)
                screen.add_widget(board)

                self.screens.append(screen)

        if self.option_style.split('-')[1] == 'switchboardVertical':
            # Add switchable ui
            self.visual = SwitchBoard(self, self.screens)

        elif self.option_style.split('-')[1] == 'allVertical':
            # Store screens in columns
            self.visual = AllBoards(self, self.screens)

        elif self.option_style.split('-')[1] == 'allHorizontal':
            # Store screens in rows
            self.visual = AllBoardsH(self, self.screens)
        
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


    # def replace_board_and_controller(self, tindex, tgame_controller, tboard_map):
    #     self.root.clear_widgets()
    #     self.screens = []
    #     self.boards = []

    #     # Create a board view for all games passed
    #     for index, game_controller in enumerate(self.game_controllers):
    #         if index == tindex:
    #             screen = Screen(name=str(tindex))
    #             board = TwoDViewBoardH(self, tgame_controller, self.user_interaction)

    #             self.boards.append(board)
    #             screen.add_widget(board)

    #             self.screens.append(screen)
    #         else:
    #             screen = Screen(name=str(index))
    #             board = TwoDViewBoardH(self, game_controller, self.user_interaction)

    #             self.boards.append(board)
    #             screen.add_widget(board)

    #             self.screens.append(screen)

    #     self.root.add_widget(AllBoardsH(self, self.screens))