from bin.Game.controller_class import GameController

import threading
import importlib
import time
from os import system, name

#'bin.Game.ControlLoops.default_star_trek_controlloop_1v1'
#'bin.Game.ControlLoops.star_trek_controlloop_1vbot'

#'bin.Game.Maps.default_star_trek_map'
#'bin.Game.Maps.checkmate.check_map'

#, 'bin.AI.AIs.nn_deep_ffnn_perceptron'

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


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

    visuals = visual_file.Visualliser(controls, option_style='2dviewHorizontal-allHorizontal', user_interaction=True)

    for i in controls:
        i.set_visualliser(visuals)

    for i in controls:
        threading._start_new_thread(i.run, ())

    visuals.run()


def main_botvbot_train_genetic(number_of_boards, ai_paths, ai_files, population=4, epochs=1, save_highest_fitness=True, verbose=False):

    controls = []

    for i in range(population):
        controls.append(GameController('game{}'.format(i), 'bin.Game.ControlLoops.star_trek_controlloop_botvbot', 'bin.Game.Maps.default_star_trek_map', *ai_paths, *ai_files, training=True, verbose=True))
    
    threads = []
    running_controls = []
    buffer = 0

    # Inits the number of boards threads and starts them
    for i in range(number_of_boards):
        threads.append(threading.Thread(target=controls[buffer].run, args=()))
        threads[-1].setDaemon(True)
        threads[-1].start()
        running_controls.append(controls[buffer])
        buffer += 1

    def thread_loop(buffer):
        # Loops until all games are complete
        while buffer < len(controls):
            time.sleep(2)

            # Checks for finished game
            threads_index = None

            for index, thread in enumerate(threads):
                if not thread.is_alive():
                    threads_index = index
                    break

            if threads_index != None:
                threads[threads_index] = threading.Thread(target=controls[buffer].run, args=())
                threads[threads_index].setDaemon(True)
                threads[threads_index].start()
                running_controls[threads_index] = controls[buffer]

                buffer += 1

        for i in threads:
            i.join()
    
    t = threading.Thread(target=thread_loop, args=(buffer,))
    t.setDaemon(True)
    t.start()

    while t.is_alive():
        time.sleep(0.1)
        clear()
        for i in running_controls:
            print(i.gamestate_str())

    
    # One population cycle complete
    fitnesses = []

    
    
    input()