__authour__ = 'Harry Burge'
__date_created__ = '10/06/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '10/06/2020'

# Imports
from bin.Utils.game_util import loops


# Attack board
class AttackBoard:
    '''
    Holds info on an attack board of where it is and which team controls it
    '''

    def __init__(self, x,y,z, team='Neutral'):

        self.x = x
        self.y = y
        self.z = z
        self.team = team


    def get_coords(self):
        return self.x, self.y, self.z


    def get_diffrence_area_coords(self):
        
        area_coords = []

        for dx, dy in loops([0,1], [0,1]):
            area_coords.append((dx, dy, 0))

        return area_coords


    def set_coords(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def valid_move_coords(self, map, ax, ay):
        '''
        params:-
            map : Map : Board of which respect to
            ax,ay : int : Poistion of attack board in the attackmap
        returns:-
            [(int,int), ...] : Suitable coords for attack board to be able to move to
        '''
        valid_moves = []

        for dx,dy in loops([-1,0,1], [-1,0,1]):
            if not(dx == dy):

                current = map.get_attack_gridpoi(ax+dx, ay+dy)

                if type(current) == tuple:
                    valid_moves.append((ax+dx, ay+dy))

        return valid_moves
                

