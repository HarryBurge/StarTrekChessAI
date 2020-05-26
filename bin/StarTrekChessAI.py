from bin.Game.controller_class import GameController

import threading
import importlib


def main():
    #'bin.Game.ControlLoops.default_star_trek_controlloop_1v1'

    #'bin.Game.Maps.default_star_trek_map'
    #'bin.Game.Maps.checkmate.check_map'

    control1 = GameController('game1', 'bin.Game.ControlLoops.default_star_trek_controlloop_1v1', 'bin.Game.Maps.default_star_trek_map')
    control2 = GameController('game2', 'bin.Game.ControlLoops.default_star_trek_controlloop_1v1', 'bin.Game.Maps.default_star_trek_map')

    visual_file = importlib.import_module('bin.Visualliser.visualliser2')

    #visuals = visual_file.Visualliser([control1])
    visuals = visual_file.Visualliser([control1, control2], option_style='2dviewVertical-allVertical')

    control1.set_visualliser(visuals)
    control2.set_visualliser(visuals)

    threading._start_new_thread(control1.run, ())
    threading._start_new_thread(control2.run, ())

    visuals.run()

    print('Use __main__.py to be able to test due to the cwd in the right place, change this main to actually to test code')
