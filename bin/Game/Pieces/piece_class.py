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


    def _rec_line(self, board, x,y,z, dx,dy,dz):
        '''
        params:-
            board : Map : board of which is respect to
            x,y,z : int : coords on board in which to check
            dx,dy,dz : int : recusivly moves along line defined by diffrences
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of all moves
                that can be made along this line after recursive call has finished
        '''
        current = board.get_gridpoi(x,y,z)

        if current in (False, 'x'):
            return []

        elif current == '@':
            return [{'coords':(x,y,z), 'mv_type':'Move'}] + self._rec_line(board, x+dx, y+dy, z+dz, dx,dy,dz)

        elif issubclass(type(current), Piece):
            if current.team != self.team:
                return [{'coords':(x,y,z), 'mv_type':'Take'}]
            else:
                return [{'coords':(x,y,z), 'mv_type':'Defending'}]

        else:
            raise SyntaxError('Invalid object or string in map')

    
    def _test_coords(self, board, coords):
        '''
        params:-
            board : Map : board of which respect too
            coords : [(int,int,int), ...] : coords to test whether piece can move, take or defend
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of all moves
                that can be made along this line after recursive call has finished
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



if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')
