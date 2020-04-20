'''
Holds super class for all peices. When creating a custom
peice, please super this class.
'''

__authour__ = 'Harry Burge'
__date_created__ = '15/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '16/04/2020'


'''
TODO:-



'''

# Code

class Piece:

    def __init__(self, coords, img_path, value=0, team='Neutral'):
        self.coords = coords
        self.team = team
        self.value = value
        self.img_path = img_path

    # Getter's
    def get_x(self):
        return self.coords[0]

    def get_y(self):
        return self.coords[1]

    def get_z(self):
        return self.coords[2]





if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')
