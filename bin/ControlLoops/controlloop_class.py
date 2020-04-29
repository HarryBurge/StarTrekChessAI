'''
ControlLoop class. Is used to read in controlloop files and be able to run them.
'''

__authour__ = 'Harry Burge'
__date_created__ = '29/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '29/04/2020'


'''
TODO:-

'''

# Imports
import importlib

import multiprocessing
multiprocessing.set_start_method('spawn')



class ControlLoop:

    def __init__(self, path, visualliser, board):
        '''
        params:-
            path : str: import path to the controlloop e.g. bin.ControlLoops.default_star_trek_controlloop_1v1
        '''
        
        # Import specfifc map
        self.controlloop_file = importlib.import_module(path)

        self.visualliser = visualliser
        self.board = board


    def run(self):

        p = multiprocessing.Process(target=self.controlloop_file.run, args=(self,))
        p.start()
        p.join()

        self.visualliser.run()

    

        


if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')