'''
A class to visualise the game and also take instructions in if feature is enabled
'''

__authour__ = 'Harry Burge'
__date_created__ = '24/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '28/04/2020'


'''
TODO:-

'''

# Imports
import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# Constants
BCKGRND_CLR = [1,1,1,0.1]
WHITE_FREE = [1,1,1,0.6]
BLACK_FREE = [1,1,1,0.4]

Builder.load_string("""
<UI>:
    cols: 1
    size_hint_x: None
    width: 40

    Button:
        id: up_level
        on_press: app.main.ids.sm.changeLevel(app.main.ids.sm.level - 1)

    Button:
        id: down_level
        on_press: app.main.ids.sm.changeLevel(app.main.ids.sm.level + 1)

<Main>:
    cols: 2

    Board:
        id: sm
        on_kv_post: self.build_board(app.board)

    UI:

<BackgroundColor@Widget>:
    background_color: 1,1,1,1
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos

<Square>:
    background_color: 1,1,1,1
    background_normal: ''
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos

    on_press: print(self.gx, self.gy, self.gz)
""")


class Visualliser(App):

    def __init__(self, board, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.board = board

    def build(self):
        self.main = Main()
        return self.main


class Main(GridLayout):
    pass

class BackgroundColor(Widget):

    def __init__(self, background_color, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_color = background_color

class UI(GridLayout):
    pass

class Square(Button):
    
    def __init__(self, gx,gy,gz, background_color, background_normal='', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_color = background_color
        self.background_normal = background_normal

        self.gx = gx
        self.gy = gy
        self.gz = gz


class Board(ScreenManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.level = 0
        self.transition = SwapTransition()

    def build_board(self, board):
        self.board = board

        for z in range(len(board.get_board())):
            temp = Screen(name='Level{}'.format(z))

            level = GridLayout(rows=len(board.get_board()[0]), cols=len(board.get_board()[0][0]))

            for y in range(len(board.get_board()[0])):
                for x in range(len(board.get_board()[0][0])):

                    current = board.get_gridpoi(x,y,z)

                    if current == 'x':
                        level.add_widget(BackgroundColor(background_color=BCKGRND_CLR))

                    elif current == '@':
                        if x%2 == 0 and y%2 == 0:
                            level.add_widget(Square(x,y,z,background_color=BLACK_FREE))
                        elif x%2 != 0 and y%2 == 0:
                            level.add_widget(Square(x,y,z,background_color=WHITE_FREE))
                        elif x%2 == 0 and y%2 != 0:
                            level.add_widget(Square(x,y,z,background_color=WHITE_FREE))
                        else:
                            level.add_widget(Square(x,y,z,background_color=BLACK_FREE))

                    else:
                        if x%2 == 0 and y%2 == 0:
                            level.add_widget(Square(x,y,z,background_color=BLACK_FREE, background_normal=current.img_path))
                        elif x%2 != 0 and y%2 == 0:
                            level.add_widget(Square(x,y,z,background_color=WHITE_FREE, background_normal=current.img_path))
                        elif x%2 == 0 and y%2 != 0:
                            level.add_widget(Square(x,y,z,background_color=WHITE_FREE, background_normal=current.img_path))
                        else:
                            level.add_widget(Square(x,y,z,background_color=BLACK_FREE, background_normal=current.img_path))

            temp.add_widget(level)

            self.add_widget(temp)

    def changeLevel(self, num):
        if num >= 0 and num < len(self.board.get_board()):
            self.level = num
            self.current = 'Level' + str(num)



if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')