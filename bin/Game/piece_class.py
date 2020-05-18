'''
Holds super class for all peices. When creating a custom
peice, please super this class.
'''

__authour__ = 'Harry Burge'
__date_created__ = '15/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '23/04/2020'


'''
TODO:-

'''


class Piece:

    def __init__(self, img_path=None, value=0, team='Neutral'):
        '''
        params:-
            img_path : str : path to folder containing images for piece based on 
                <team>-<piecename>.png
            value : int : value assigned to piece, used for scoring and AI
            team : str : team of which piece is assigned too
        '''
        self.team = team
        self.value = value
        self.img_path = img_path


    def _rec_line_3D(self, board, x,y,z, dx,dy,dz):
        '''
        params:-
            board : Map : board of which is respect to
            x,y,z : int : coords on board in which to check
            dx,dy,dz : int : recusivly moves along line defined by diffrences
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of all moves
                that can be made along this line after recursive call has finished
        '''
        temp = self._test_coord(board, x,y,z)

        if not temp:
            return []

        elif temp['mv_type'] == 'Move':
            return [temp] + self._rec_line_3D(board, x+dx, y+dy, z+dz, dx,dy,dz)

        else:
            return [temp]


    def _rec_line_StarTrek(self, board, x,y,z, dx,dy):
        '''
        params:-
            board : Map : board of which is respect to
            x,y,z : int : coords on board in which to check
            dx,dy,dz : int : recusivly moves along line defined by diffrences
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of all moves
                that can be made along this line after recursive call has finished
                can have duplicates
        '''
        current = self._test_coord(board, x,y,z)

        if current == False:
            return []

        elif current['mv_type'] == 'Move':
            temp = []

            for dz in [-1,0,1]:
                temp += self._rec_line_StarTrek(board, x+dx, y+dy, z+dz, dx, dy)
            return [current] + temp

        else:
            temp = []

            for dz in [-1,1]:
                temp += self._rec_line_StarTrek(board, x+dx, y+dy, z+dz, dx, dy)
            return [current] + temp

    
    def _test_coords(self, board, coords):
        '''
        params:-
            board : Map : board of which respect too
            coords : [(int,int,int), ...] : coords to test whether piece can't/can move,
                take or defend
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : Checks whether the peice
                if able to get that coord whether it can due to other entitys
        '''
        tested_moves = []

        for x,y,z in coords:

            current = board.get_gridpoi(x,y,z)

            if current in (False, 'x'):
                pass

            elif current == '@':
                tested_moves += [{'coords':(x,y,z), 'mv_type':'Move'}]

            elif issubclass(type(current), Piece):
                if current.team != self.team:
                    tested_moves += [{'coords':(x,y,z), 'mv_type':'Take'}]
                else:
                    tested_moves += [{'coords':(x,y,z), 'mv_type':'Defending'}]

            else:
                raise SyntaxError('Invalid object or string in map')

        return tested_moves


    def _test_coord(self, board, x,y,z):
        '''
        params:-
            board : Map : board of which respect too
            x,y,z : int : coords to test whether piece can't/can move, take or defend
        returns:-
            {'coords' : (int,int,int), 'mv_type' : str} : Checks whether the peice
                if able to get that coord whether it can due to other entitys
        '''

        current = board.get_gridpoi(x,y,z)

        if current in (False, 'x'):
            return False

        elif current == '@':
            return {'coords':(x,y,z), 'mv_type':'Move'}

        elif issubclass(type(current), Piece):
            if current.team != self.team:
                return {'coords':(x,y,z), 'mv_type':'Take'}
            else:
                return {'coords':(x,y,z), 'mv_type':'Defending'}

        else:
            raise SyntaxError('Invalid object or string in map')



if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')
