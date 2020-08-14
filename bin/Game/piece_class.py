__authour__ = 'Harry Burge'
__date_created__ = '15/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '18/05/2020'


# Piece
class Piece:
    '''
    Holds super class for all peices. 
    
    Info:-
        -When creating a custom peice, please super this class
        -Due to StarTrekChess not actually being 3D in terms of mechanics
            there has to be a seperate rec_line function for when someone
            wants to create a diffrent board and normal 3D movement
        -New pieces need to have a valid_move_coords function
    '''

    def __init__(self, img_path=None, value=0, team='Neutral'):
        '''
        params:-
            img_path : str : Path to folder containing images for piece based on 
                <team>-<piecename>.png
            value : int : Value assigned to piece, this is arbitrary
            team : str : Team of which piece belongs too
        '''
        self.team = team
        self.value = value
        self.img_path = img_path

    
    # Super Class things
    def valid_move_coords(self, board, x,y,z):
        '''
        params:-
            board : Map : Board with respect to
            x,y,z : int : Coords of piece
        returns:-
            [] : This needs to get overidden by custom pieces but here just
                incase someone doesn't
        '''
        return []


    # Funcs
    def rec_line_3D(self, board, x,y,z, dx,dy,dz):
        '''
        params:-
            board : Map : Board of which is respect to
            x,y,z : int : Coords on board to check on this recursive call
            dx,dy,dz : int : Recusivly moves along line defined by diffrences
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of all moves
                that can be made along this line after recursive call has finished
        '''
        current = self.test_coord(board, x,y,z)

        if current == False:
            return []

        # Due to freely moveable it can carry along line
        elif current['mv_type'] == 'Move':
            return [current] + self.rec_line_3D(board, x+dx, y+dy, z+dz, dx,dy,dz)

        else:
            return [current]


    def rec_line_StarTrek(self, board, x,y,z, dx,dy, _tested_coords):
        '''
        params:-
            board : Map : Board of which is respect to
            x,y,z : int : Coords on board to check on this recursive call
            dx,dy : int : Recusivly moves along line defined by diffrences
            _tested_coords : [] : Has to be passed in due to acting like a global
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : List of all moves
                that can be made along this line after recursive call has finished.
                Due to StarTrekChess in mechanice actually being 2D it will also check
                -+1 dz so duplicate coords will be created in situations like a piece
                on the line a free space above and below. This needs to be accounted
                for whilst using this function.
        '''
        if (x,y,z) in _tested_coords:
            return []
        else:
            _tested_coords.append((x,y,z))

            current = self.test_coord(board, x,y,z)

            temp = []

            if current == False:
                return []

            elif current['mv_type'] == 'Move':
                # Same as rec_line_3D but now has to account for that -+1 diffrence in z
                for dz in [-1,0,1]:
                    temp += self.rec_line_StarTrek(board, x+dx, y+dy, z+dz, dx, dy, _tested_coords)

            else:
                # Same as rec_line_3D but now has to account for that -+1 diffrence in z
                for dz in [-1,1]:
                    temp += self.rec_line_StarTrek(board, x, y, z+dz, dx, dy, _tested_coords)

            return [current] + temp


    def test_coord(self, board, x,y,z):
        '''
        params:-
            board : Map : Board of which respect too
            x,y,z : int : Coords to test on
        returns:-
            False|{'coords' : (int,int,int), 'mv_type' : str} : Checks whether the peice
                if able to get that coord whether it can due to other entitys.
                Like if they are the same team or not a poistion at all
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


    def test_coords(self, board, coords):
        '''
        params:-
            board : Map : Board of which respect too
            coords : [(int,int,int), ...] : Coordinates to test on, plural of test_coord
        returns:-
            [{'coords' : (int,int,int), 'mv_type' : str}, ...] : Checks whether the peice
                if able to get that coord whether it can due to other entitys, repeatative
                version of test_coord
        '''
        tested_moves = []

        for coord in coords:

            current = self.test_coord(board, *coord)

            if current != False:
                tested_moves.append(current)

        return tested_moves


if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')
