from bin.Game.controller_class import GameController

import threading
import importlib
import time
import random
import copy
import numpy
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


def main_botvbot_train_genetic(number_of_boards, ai_paths, ai_files, population=4, epochs=4, save_highest_fitness=True, verbose=False):

    average_fitness_epoch = []
    top_fitness_epoch = []

    # One population cycle
    current_pop_controls = []

    for i in range(population):
        current_pop_controls.append(GameController('game{}'.format(i), 'bin.Game.ControlLoops.star_trek_controlloop_botvbot', 'bin.Game.Maps.default_star_trek_map', *ai_paths, *ai_files, training=True, verbose=True))
    
    for e in range(epochs):
        threads = []
        running_current_pop_controls = []
        buffer = 0

        # Inits the number of boards threads and starts them
        for i in range(number_of_boards):
            threads.append(threading.Thread(target=current_pop_controls[buffer].run, args=()))
            threads[-1].setDaemon(True)
            threads[-1].start()
            running_current_pop_controls.append(current_pop_controls[buffer])
            buffer += 1

        def thread_loop(buffer):
            # Loops until all games are complete
            while buffer < len(current_pop_controls):
                time.sleep(2)

                # Checks for finished game
                threads_index = None

                for index, thread in enumerate(threads):
                    if not thread.is_alive():
                        threads_index = index
                        break

                if threads_index != None:
                    threads[threads_index] = threading.Thread(target=current_pop_controls[buffer].run, args=())
                    threads[threads_index].setDaemon(True)
                    threads[threads_index].start()
                    running_current_pop_controls[threads_index] = current_pop_controls[buffer]

                    buffer += 1

            for i in threads:
                i.join()
        
        t = threading.Thread(target=thread_loop, args=(buffer,))
        t.setDaemon(True)
        t.start()

        while t.is_alive():
            time.sleep(0.1)
            clear()
            for i in running_current_pop_controls:
                print(i.gamestate_str())

        
        # Calc fitness of completed games
        fitnesses = []

        for i in current_pop_controls:
            fitnesses.append(i.score()[0])

        # Save the max of that population
        top_index = fitnesses.index(max(fitnesses))
        current_pop_controls[top_index].get_ai_controller()[0].save_weights_and_biass('bin/AI/AIs/nn_deep_ffnn_perceptron_wb/ai_' + str(e) + '.h5')

        # Change fitness into all sum == 1 for random choice weights
        pop_fitness = 0.01
        for i in fitnesses:
            pop_fitness += i

        # Stats
        top_fitness_epoch.append(max(fitnesses))
        average_fitness_epoch.append(pop_fitness/population)
        # ----

        for i in range(len(fitnesses)):
            fitnesses[i] = fitnesses[i]/pop_fitness

        # Generate new population based on fitness of old
        new_pop_controls = []

        for i in range(population):
            
            # Pick two random bots in current_pop
            ran_control1 = random.choices(current_pop_controls, fitnesses)[0]
            ran_control2 = random.choices(current_pop_controls, fitnesses)[0]

            # Need to make AI weights into the layer thing
            new_control = GameController('game{}'.format(i), 'bin.Game.ControlLoops.star_trek_controlloop_botvbot', 'bin.Game.Maps.default_star_trek_map', *ai_paths, None, 'bin/AI/AIs/nn_deep_ffnn_perceptron_wb/ai_' + str(e) + '.h5', training=True, verbose=True)

            bot1 = ran_control1.get_ai_controller()[0]
            bot2 = ran_control2.get_ai_controller()[0]

            # Loop every weight and breed with mutations
            for j in range(5):

                newwb = copy.deepcopy(bot1.model.get_layer(index=j).get_weights())
                bot2wb = bot2.model.get_layer(index=j).get_weights()

                for x in range(len(newwb[0])):
                    for k in range(len(newwb[0][x])):

                        if random.randint(0, 1) == 0:
                            newwb[0][x].itemset(k, bot2wb[0][x,k])

                        if random.randint(0, 100) < 5:
                            newwb[0][x].itemset(k, random.uniform(-1, 1))

                new_control.get_ai_controller()[0].model.get_layer(index=j).set_weights(newwb)

            new_pop_controls.append(new_control)

        current_pop_controls = new_pop_controls

        #generate random population
        #run population
        #calculate fitness
        #generate new population
        #   based of fitness do random with a half normal distibution style of thing
        #   make sure there is mutation
        # repeat but against new pop and the second bot is the max fitness from prevouis

    clear()
    print('-----Stats------')
    for i in range(len(average_fitness_epoch)):
        print(str(i) + 'top= ' + str(top_fitness_epoch[i]) + '  avg= ' + str(average_fitness_epoch[i]))
    input('-------End-------')