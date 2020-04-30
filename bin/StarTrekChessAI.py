from bin.Game.Maps import map_class
from bin.Visualliser import visualliser
from bin.ControlLoops import controller_class


def main():
    map1 = map_class.Map('bin.Game.Maps.default_star_trek_map')

    control = controller_class.GameController('bin.ControlLoops.default_star_trek_controlloop_1v1', map1)

    control.run()


    print('Use __main__.py to be able to test due to the cwd in the right place, change this main to actually to test code')
    pass
