import time
import copy

from random import randint

from bin.Game.Pieces.StarTrekChess.king_s import King
from bin.Game.Pieces.StarTrekChess.pawn_s import Pawn


class ControlLoop: # Stop loops happening within the game

    def __init__(self):
        self.players = ['White', 'Black']
        self.turn = 0
        self.count = 0
        self.history = []
        self.players_check_count = [0,0]

    def run(self, GameController, AIS, training=False):

        loop = True
        time.sleep(2)

        GameController.update_board(GameController.get_map())

        while loop:
            time.sleep(0.2)

            # Bots go
            coords1, coords2 = AIS[self.turn].suggest_move(GameController.get_map(), self.players[self.turn])
            self.count += 1

            if coords1==False or coords2==False:
                print('Bad suggestion')

            elif GameController.do_move(*coords1, *coords2, self.players[self.turn], [Pawn], King):
                GameController.update_board(GameController.get_map())
                self.history.append((coords1, coords2))
                print('Bot made succsesful move', self.count)

                if self.turn < len(self.players) - 1:
                    self.turn += 1
                else:
                    self.turn = 0

            if GameController.is_in_check(self.players[self.turn], King):
                print(self.players[self.turn] + ' is in check')
                if training:
                    self.players_check_count[self.turn] += 1

                if GameController.is_in_checkmate(self.players[self.turn], King):
                    print(self.players[self.turn] + ' is in checkmate')
                    loop = False

            if self.if_repeats(self.history):
                print('There is over 3 repeated moves in history')
                loop = False

            if training and max(self.players_check_count) > 6:
                print(self.players[self.turn] + ' has been checked 6 times')
                loop = False

    
    def if_repeats(self, moves, num_of_repeats=3):
        for index, move in enumerate(moves):
            if move in moves[:index] + moves[index+1:]:
                break
        else:
            return False

        num_of_repeats -= 1
        if num_of_repeats == 1:
            return True
        else:
            return self.if_repeats(moves[:index] + moves[index+1:], num_of_repeats)