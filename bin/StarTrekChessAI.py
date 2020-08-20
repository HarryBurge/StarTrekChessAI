from bin.Game.controller_class import GameController

import threading
import importlib

#'bin.Game.ControlLoops.default_star_trek_controlloop_1v1'
#'bin.Game.ControlLoops.star_trek_controlloop_1vbot'

#'bin.Game.Maps.default_star_trek_map'
#'bin.Game.Maps.checkmate.check_map'

#, 'bin.AI.AIs.nn_deep_ffnn_perceptron'


def main_1v1():

    controls = []

    for i in range(1):
        controls.append(GameController('game{}'.format(i), 'bin.Game.ControlLoops.default_star_trek_controlloop_1v1', 'bin.Game.Maps.default_star_trek_map'))

    visual_file = importlib.import_module('bin.Visualliser.visualliser2')

    visuals = visual_file.Visualliser(controls, option_style='2dviewHorizontal-allHorizontal')

    for i in controls:
        i.set_visualliser(visuals)

    for i in controls:
        threading._start_new_thread(i.run, ())

    visuals.run()


def main_1vbot():

    controls = []

    for i in range(1):
        controls.append(GameController('game{}'.format(i), 'bin.Game.ControlLoops.star_trek_controlloop_1vbot', 'bin.Game.Maps.default_star_trek_map', 'bin.AI.AIs.nn_deep_ffnn_perceptron'))

    visual_file = importlib.import_module('bin.Visualliser.visualliser2')

    visuals = visual_file.Visualliser(controls, option_style='2dviewHorizontal-allHorizontal')

    for i in controls:
        i.set_visualliser(visuals)

    for i in controls:
        threading._start_new_thread(i.run, ())

    visuals.run()


def main_botvbot():

    controls = []

    for i in range(1):
        controls.append(GameController('game{}'.format(i), 'bin.Game.ControlLoops.star_trek_controlloop_botvbot', 'bin.Game.Maps.default_star_trek_map', 'bin.AI.AIs.nn_deep_ffnn_perceptron', 'bin.AI.AIs.nn_deep_ffnn_perceptron'))

    visual_file = importlib.import_module('bin.Visualliser.visualliser2')

    visuals = visual_file.Visualliser(controls, option_style='2dviewHorizontal-allHorizontal')

    for i in controls:
        i.set_visualliser(visuals)

    for i in controls:
        threading._start_new_thread(i.run, ())

    visuals.run()


def main_botvbot_train(number_of_boards, ai_paths, ai_files):
    print(number_of_boards, ai_paths, ai_files)
    input()