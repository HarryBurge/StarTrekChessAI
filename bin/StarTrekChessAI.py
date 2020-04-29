from bin.Game.Maps import map_class
from bin.Visualliser import visualliser
from bin.ControlLoops import controlloop_class


def main():
    map1 = map_class.Map('bin.Game.Maps.default_star_trek_map')

    tom = visualliser.Visualliser(map1)

    control = controlloop_class.ControlLoop('bin.ControlLoops.default_star_trek_controlloop_1v1', tom, map1)

    control.run()


    print('Use __main__.py to be able to test due to the cwd in the right place, change this main to actually to test code')
    pass
