from bin.Game.map_class import Map 
from bin.Game.controller_class import GameController
from bin.Visualliser import visualliser


def main():
    #map1 = Map('bin.Game.Maps.default_star_trek_map')

    map1 = Map('bin.Game.Maps.checkmate_check_map')

    control = GameController('bin.Game.ControlLoops.default_star_trek_controlloop_1v1', map1)

    control.run()


    print('Use __main__.py to be able to test due to the cwd in the right place, change this main to actually to test code')
    pass
