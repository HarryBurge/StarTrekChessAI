import time
import copy

from bin.Game.Pieces.StarTrekChess.king_s import King
from bin.Game.Pieces.StarTrekChess.pawn_s import Pawn


class ControlLoop:

    def __init__(self):
        self.players = ['White', 'Black']
        self.turn = 0

    def run(self, GameController):

        loop = True

        while loop:
            time.sleep(0.2)

            if len(GameController.instructions) == 1:

                if GameController.show_valid_moves(*GameController.instructions[0], self.players[self.turn]):
                    pass
                else:
                    print('First choice is wrong. Still ' + self.players[self.turn] + '\'s turn.')
                    GameController.instructions = []


            elif len(GameController.instructions) == 2:

                if GameController.do_move(*GameController.instructions[0], *GameController.instructions[1], self.players[self.turn], [Pawn], King):
                    if self.turn < len(self.players) - 1:
                        self.turn += 1
                    else:
                        self.turn = 0

                else:
                    print('Bad second choice. Still ' + self.players[self.turn] + '\'s turn.')
                    GameController.update_board(GameController.get_map())

                GameController.instructions = []


            # if GameController.is_in_check(self.players[self.turn], King):
            #     print(self.players[self.turn] + ' is in check')

            #     if GameController.is_in_checkmate(self.players[self.turn], King):
            #         print(self.players[self.turn] + ' is in checkmate')
            #         loop = False