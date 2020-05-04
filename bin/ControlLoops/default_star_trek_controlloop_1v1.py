import time
import copy

class ControlLoop:

    def __init__(self):
        self.players = ['White', 'Black']
        self.turn = 0

    def run(self, GameController):
        while True:
            time.sleep(0.1)

            if len(GameController.instructions) == 1:

                if self._showValidMoves_check(GameController.board, *GameController.instructions[0]):

                    board = copy.deepcopy(GameController.board)
                    validmoves = board.get_gridpoi(*GameController.instructions[0]).valid_move_coords(board, *GameController.instructions[0])

                    for i in validmoves:
                        if i['mv_type'] == 'Defending':
                            board.set_gridpoi(*i['coords'], ['D', board.get_gridpoi(*i['coords'])])

                        elif i['mv_type'] == 'Move':
                            board.set_gridpoi(*i['coords'], ['M', board.get_gridpoi(*i['coords'])])

                        elif i['mv_type'] == 'Take':
                            board.set_gridpoi(*i['coords'], ['T', board.get_gridpoi(*i['coords'])])

                    GameController.visualliser.update_board(board)


                else:
                    print('First choice is wrong. Still ' + self.players[self.turn] + '\'s turn.')
                    GameController.instructions = []


            elif len(GameController.instructions) == 2:

                if self._doMove_check(GameController.board, *GameController.instructions[0], *GameController.instructions[1]):
                    GameController.board.move_piece(*GameController.instructions[0], *GameController.instructions[1])
                    GameController.visualliser.update_board(GameController.board)

                    if self.turn < len(self.players) - 1:
                        self.turn += 1
                    else:
                        self.turn = 0

                else:
                    print('Bad second choice. Still ' + self.players[self.turn] + '\'s turn.')
                    GameController.visualliser.update_board(GameController.board)

                GameController.instructions = []


    def _doMove_check(self, board, x1,y1,z1, x2,y2,z2):
        '''
        params:-
            board : Map : board into respect of
            x2,y2,z2 : int : gridpoi of thing to move to
        '''
        if board.get_gridpoi(x2,y2,z2) in [False, 'x']:
            return False

        elif board.get_gridpoi(x2,y2,z2) == '@':
            if self._in_valid_moves(board.get_gridpoi(x1,y1,z1).valid_move_coords(board, x1,y1,z1), x2,y2,z2, ('Take', 'Move')):
                return True
            else:
                return False

        elif board.get_gridpoi(x2,y2,z2).team != self.players[self.turn]:
            if self._in_valid_moves(board.get_gridpoi(x1,y1,z1).valid_move_coords(board, x1,y1,z1), x2,y2,z2, ('Take', 'Move')):
                return True
            else:
                return False

        else:
            return False


    def _showValidMoves_check(self, board, x1,y1,z1):
        '''
        params:-
            board : Map : board into respect of
            x1,y1,z1 : int : gridpoi of thing selected
        '''
        if board.get_gridpoi(x1,y1,z1) in [False, 'x', '@']:
            return False

        elif board.get_gridpoi(x1,y1,z1).team == self.players[self.turn]:
            return True

        else: 
            return False
    
    def _in_valid_moves(self, moves, x2,y2,z2, mv_type):
        
        found = False

        for i in moves:
            if i['mv_type'] in mv_type and i['coords'] == (x2,y2,z2):
                found = True

        return found


