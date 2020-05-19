from bin.Game.map_class import Map 
from bin.Game.controller_class import GameController
from bin.Visualliser import visualliser

import threading


def main():
    #'bin.Game.ControlLoops.default_star_trek_controlloop_1v1'

    #'bin.Game.Maps.default_star_trek_map'
    #'bin.Game.Maps.checkmate.check_map'

    #'bin.Visualliser.visualliser'

    control1 = GameController('game1', 'bin.Game.ControlLoops.default_star_trek_controlloop_1v1', 'bin.Game.Maps.default_star_trek_map', 'bin.Visualliser.visualliser')
    #control2 = GameController('game2', 'bin.Game.ControlLoops.default_star_trek_controlloop_1v1', 'bin.Game.Maps.default_star_trek_map')

    control1.run()
    #control2.run()

    #threading._start_new_thread(control1.run, ())
    #threading._start_new_thread(control2.run, ())

    # while True:
    #     pass


    print('Use __main__.py to be able to test due to the cwd in the right place, change this main to actually to test code')
    pass
