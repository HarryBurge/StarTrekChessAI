from bin.Game.controller_class import GameController

import threading
import importlib


def main():
    #'bin.Game.ControlLoops.default_star_trek_controlloop_1v1'

    #'bin.Game.Maps.default_star_trek_map'
    #'bin.Game.Maps.checkmate.check_map'

    controls = []

    for i in range(10):
        controls.append(GameController('game{}'.format(i), 'bin.Game.ControlLoops.default_star_trek_controlloop_1v1', 'bin.Game.Maps.default_star_trek_map'))

    visual_file = importlib.import_module('bin.Visualliser.visualliser2')

    #visuals = visual_file.Visualliser([control1])
    visuals = visual_file.Visualliser(controls, option_style='2dviewVertical-allVertical')


    for i in controls:
        i.set_visualliser(visuals)

    for i in controls:
        threading._start_new_thread(i.run, ())

    visuals.run()

    print('Use __main__.py to be able to test due to the cwd in the right place, change this main to actually to test code')
