__authour__ = 'Harry Burge'
__date_created__ = '29/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '18/05/2020'

# Imports
import importlib
import threading

from bin.Visualliser import visualliser
from bin.Game.map_class import Map


# GameController
class GameController:
    '''
    Is used to read in controlloop files and be able to run them.

    Info:-
        -Control loop files need to have a run function which is a loop
        due to kivy stopping all execution on run thread.
    '''

    def __init__(self, controlloop_path, map_path, visualliser_path=None):
        '''
        params:-
            controlloop_path : str : Import path to the controlloop 
                e.g. bin.ControlLoops.default_star_trek_controlloop_1v1
            map_path : str : Import path to the map
            visualliser_path : None|str : If none then no visuals else
                import path to the visualliser (This is a placeholder for 
                when there are diffrent visuals and if simulating without one)
        '''
        # Import specfifc control loop and visualliser if required
        self.controlloop = importlib.import_module(controlloop_path).ControlLoop()

        if visualliser_path != None:
            self.visualliser = importlib.import_module(visualliser_path).Visualliser(map, self)
        else:
            self.visualliser = None

        self.map = Map(map_path)
        self.instructions = []


    def run(self):
        '''
        params:- 
            None
        returns:-
            None
        '''
        threading._start_new_thread(self.controlloop.run, (self,))

        if self.visualliser != None:
            threading._start_new_thread(self.visualliser.run(), ())


    def clicked(self, x,y,z):
        '''
        params:-
            x,y,z : int : Grid coordinates clicked on
                (Only used for when you have a UI)
        returns:-
            None
        '''
        self.instructions.append([x,y,z])
 

if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')