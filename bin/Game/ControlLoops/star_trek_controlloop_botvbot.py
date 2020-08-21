import time
import copy
from os import system, name

from random import randint

from bin.Game.Pieces.StarTrekChess.king_s import King
from bin.Game.Pieces.StarTrekChess.pawn_s import Pawn
from bin.Game.Pieces.StarTrekChess.castle_s import Castle
from bin.Game.Pieces.StarTrekChess.bishop_s import Bishop
from bin.Game.Pieces.StarTrekChess.knight_s import Knight
from bin.Game.Pieces.StarTrekChess.queen_s import Queen


class ControlLoop: # Stop loops happening within the game

    def __init__(self, training, verbose):
        self.players = ['White', 'Black']
        self.turn = 0
        self.count = 0
        self.history = []
        self.messages = []
        self.players_check_count = [0,0]
        self.training = training
        self.verbose = verbose

    def run(self, GameController, AIS):

        loop = True
        time.sleep(2)

        GameController.update_board(GameController.get_map())

        while loop:

            # Bots go
            coords1, coords2 = AIS[self.turn].suggest_move(GameController.get_map(), self.players[self.turn])
            self.count += 1

            if coords1==False or coords2==False:
                self.messages.append('Bad suggestion')

            elif GameController.do_move(*coords1, *coords2, self.players[self.turn], [Pawn], King):
                GameController.update_board(GameController.get_map())
                self.history.append((coords1, coords2))
                # self.messages.append('Bot made succsesful move' + str(self.count))

                if self.turn < len(self.players) - 1:
                    self.turn += 1
                else:
                    self.turn = 0

            if GameController.is_in_check(self.players[self.turn], King):
                self.messages.append(self.players[self.turn] + ' is in check')
                if self.training:
                    self.players_check_count[self.turn] += 1

                if GameController.is_in_checkmate(self.players[self.turn], King):
                    self.messages.append(self.players[self.turn] + ' is in checkmate')
                    loop = False

            if self.if_repeats(self.history):
                self.messages.append('There is over 3 repeated moves in history')
                loop = False

            if self.training and max(self.players_check_count) > 6:
                self.messages.append(self.players[self.turn] + ' has been checked 6 times')
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

        
    def gamestate_str(self, GameController):
        gamesstate = '------Game ' + str(GameController.id) + '------\n\n'

        board = GameController.get_map()
        
        for x in range(board._size[0]):

            for z in range(board._size[2]):
                for y in range(board._size[1]):

                    if board.get_gridpoi(x,y,z) == False:
                        gamesstate += ' NA '
                    elif board.get_gridpoi(x,y,z) == '@':
                        gamesstate += ' @  '
                    elif type(board.get_gridpoi(x,y,z)) == Pawn:
                        gamesstate += ' ' + board.get_gridpoi(x,y,z).team[0] + 'p '
                    elif type(board.get_gridpoi(x,y,z)) == Knight:
                        gamesstate += ' ' + board.get_gridpoi(x,y,z).team[0] + 'k '
                    elif type(board.get_gridpoi(x,y,z)) == Bishop:
                        gamesstate += ' ' + board.get_gridpoi(x,y,z).team[0] + 'b '
                    elif type(board.get_gridpoi(x,y,z)) == Castle:
                        gamesstate += ' ' + board.get_gridpoi(x,y,z).team[0] + 'c '
                    elif type(board.get_gridpoi(x,y,z)) == Queen:
                        gamesstate += ' ' + board.get_gridpoi(x,y,z).team[0] + 'q '
                    elif type(board.get_gridpoi(x,y,z)) == King:
                        gamesstate += ' ' + board.get_gridpoi(x,y,z).team[0] + 'K '
                    else:
                        gamesstate += '    '
                
            gamesstate += '\n'

        if len(self.history) > 3:
            gamesstate += '\n------History------\n' + str(self.history[-3]) + '\n' + str(self.history[-2]) + '\n' + str(self.history[-1])

        gamesstate += '\n------Messages------\n'

        for i in self.messages:
            gamesstate += i + '\n'

        return gamesstate