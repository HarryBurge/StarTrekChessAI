'''
ControlLoop class. Is used to read in controlloop files and be able to run them.
'''

__authour__ = 'Harry Burge'
__date_created__ = '29/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '30/04/2020'


'''
TODO:-

'''

# Imports
import importlib
import threading
from bin.Visualliser import visualliser


class GameController:

    def __init__(self, path, board):
        '''
        params:-
            path : str: import path to the controlloop e.g. bin.ControlLoops.default_star_trek_controlloop_1v1
        '''
        
        # Import specfifc map
        self.controlloop_file = importlib.import_module(path).ControlLoop()

        self.visualliser = visualliser.Visualliser(board, self)

        self.board = board
        self.instructions = []


    def run(self):
        threading._start_new_thread(self.controlloop_file.run, (self,))
        threading._start_new_thread(self.visualliser.run(), ())


    def clicked(self, gx,gy,gz):
        self.instructions.append([gx,gy,gz])
 


if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')