import time

class ControlLoop:

    def __init__(self):
        self.players = ['White', 'Black']
        self.turn = 0
        self.instrucions = []

    def run(self, GameController):
        while True:
            time.sleep(0.1)

            if len(self.instrucions) == 1:
                print('boradthing')
            elif len(self.instrucions) == 2:
                print('control logic for a move')
                self.instrucions = []
            else:
                print('waiting')
                pass

    def clicked(self, gx,gy,gz):
        self.instrucions.append([gx,gy,gz])


        #GameController.board.move_piece(gx,gy,gz, 0,0,0)
        #GameController.visualliser.update_board(GameController.board)
    

