__authour__ = 'Harry Burge'
__date_created__ = '29/04/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '18/05/2020'

# Imports
import importlib
import copy

from bin.Game.map_class import Map
from bin.Game.piece_class import Piece
from bin.Game.attack_board_class import AttackBoard

from bin.Game.Pieces.StarTrekChess.king_s import King


# GameController
class GameController:
    '''
    Is used to read in controlloop files and be able to run them.

    Info:-
        -Control loop files need to have a run function which is a loop
        due to kivy (This is cause of the current visualliser using kivy)
        stopping all execution on run thread.
        -Visualliser needs to have run option
        -Visualliser file needs to have a class Visualliser
        -Visualliser needs to have update_board(<Map>) also needs to be able
        to handle showing valid move coords which comes in the form
        ['M'|'D'|'T', str|Piece_subclass]
    '''

    def __init__(self, id, controlloop_path, map_path, ai_path=None, ai_path2=None, ai_save=None, ai2_save=None, training=False, verbose=False):
        '''
        params:-
            controlloop_path : str : Import path to the controlloop 
                e.g. bin.ControlLoops.default_star_trek_controlloop_1v1
            map_path : str : Import path to the map
            ai_path : str : Import path to the AI
        '''
        # Import specfifc control loop
        if not training:
            self.controlloop = importlib.import_module(controlloop_path).ControlLoop()
        else:
            self.controlloop = importlib.import_module(controlloop_path).ControlLoop(training=True, verbose=verbose)

        # Create specfic map
        self.map = copy.deepcopy(Map(map_path))

        # Import AI
        if ai_path == None:
            self.AIController = None
        elif ai_path2 == None:
            self.AIController = importlib.import_module(ai_path).Bot(ai_save)
        else:
            self.AIController= [importlib.import_module(ai_path).Bot(ai_save), importlib.import_module(ai_path2).Bot(ai2_save)]

        self.visualliser = None

        self.id = id
        self.instructions = []


    # Getters
    def get_id(self):
        return self.id

    def get_controlloop(self):
        return self.controlloop

    def get_map(self):
        return self.map
    
    def get_visualliser(self):
        if self.visualliser == None:
            return False
        return self.visualliser

    def get_ai_controller(self):
        if self.AIController == None:
            return False
        else:
            return self.AIController

    
    # Setters
    def set_visualliser(self, visualliser):
        self.visualliser = visualliser


    # Interfaces
    # Map getters
    def get_gridpoi(self, x, y, z):
        return self.get_map().get_gridpoi(x,y,z)

    def get_attack_gridpoi(self, ax, ay):
        return self.get_map().get_attack_gridpoi(ax, ay)

    def get_valid_move_coords(self, x,y,z):
        return self.get_gridpoi(x,y,z).valid_move_coords(self.get_map(), x,y,z)
    
    def get_all_pieces(self):
        return self.get_map().get_all_pieces()

    # Map setters
    def set_gridpoi(self, x,y,z, piece):
        return self.get_map().set_gridpoi(x,y,z, piece)

    def set_attack_gridpoi(self, ax, ay, board):
        return self.get_map().set_attack_gridpoi(ax, ay, board)

    # Map funcs
    def move_piece(self, x1,y1,z1, x2,y2,z2):
        return self.get_map().move_piece(x1,y1,z1, x2,y2,z2)

    def move_attack_board(self, ax1, ay1, ax2, ay2):
        return self.get_map().move_attack_board(ax1, ay1, ax2, ay2)

    def is_in_check(self, team, king_class):
        return self.get_map().is_in_check(team, king_class)

    def is_in_checkmate(self, team, king_class):
        return self.get_map().is_in_checkmate(team, king_class)

    # Visulliser funcs
    def update_board(self, board):
        if self.get_visualliser() == False:
            return False
        return self.get_visualliser().update_board(self, board)


    # Starter
    def run(self):
        '''
        params:- 
            None
        returns:-
            True : Starts up code execution of the gamecontroller
        '''
        if self.get_ai_controller() == False:
            self.get_controlloop().run(self)
        else:
            self.get_controlloop().run(self, self.get_ai_controller())

        return True


    # UI - Passing
    def clicked(self, x,y,z):
        '''
        params:-
            x,y,z : int|str : Grid coordinates clicked on
                (Only used for when you have a UI)
        returns:-
            None
        '''
        self.instructions.append([x,y,z])


    # Comaparitors
    def is_in_valid_moves(self, moves, x,y,z, mv_type):
        '''
        params:-
            moves : [{'coords' : (int,int,int), 'mv_type' : str}, ...] : Moves 
                to search through
            x,y,z : int : Coords to search through
            mv_type : [str, ...] : If coord and one of mv_type
        returns:-
            bool : True is found in moves and False if not
        '''
        found = False

        for i in moves:
            if i['mv_type'] in mv_type and i['coords'] == (x,y,z):
                found = True

        return found


    def is_team(self, x,y,z, teams_turn):
        '''
        params:-
            x,y,z : int : Gridpoi of thing selected
            teams_turn : str : Teams turn
        returns:-
            bool : True if thing at x,y,z is the same teams as teams_turn
                False otherwise
        '''
        current = self.get_gridpoi(x,y,z)

        if issubclass(type(current), Piece) and current.team == teams_turn:
            return True
        return False


    def can_move(self, x1,y1,z1, x2,y2,z2, teams_turn):
        '''
        params:-
            x1,y1,z1 : int : Moving piece
            x2,y2,z2 : int : Place to move to
            teams_turn : str : Current teams turn
        returns:-
            bool : True if move can be made else False
        '''
        current = self.get_gridpoi(x1,y1,z1)

        if issubclass(type(current), Piece) and self.is_in_valid_moves(
                                                    self.get_valid_move_coords(x1,y1,z1), 
                                                    x2,y2,z2,
                                                    ('Take', 'Move')):
            return True
        return False


    # Funcs
    def show_valid_moves(self, x,y,z, teams_turn):
        '''
        params:-
            x,y,z : int : Coords on board to show valid moves of
            teams_turn : What teams turn is it
        returns:-
            bool : True if its shown the valid moves on the board
                False if its failed due to coords being wrong, not being a piece
                or even a visualliser not exsiting
        '''
        if self.get_visualliser() != False and self.is_team(x,y,z, teams_turn):

            simulated_map = copy.deepcopy(self.get_map())
            validmoves = simulated_map.get_gridpoi(x,y,z).valid_move_coords(simulated_map, x,y,z)

            # For all moves change the copied boards coords to have a list that can later be used
            # by a visualliser to show valid move coords
            for i in validmoves:

                if i['mv_type'] == 'Defending':
                    simulated_map.set_gridpoi( *i['coords'], 
                                                ['D', simulated_map.get_gridpoi(*i['coords'])])

                elif i['mv_type'] == 'Move':
                    simulated_map.set_gridpoi( *i['coords'], 
                                                ['M', simulated_map.get_gridpoi(*i['coords'])])

                elif i['mv_type'] == 'Take':
                    simulated_map.set_gridpoi( *i['coords'], 
                                                ['T', simulated_map.get_gridpoi(*i['coords'])])

            # Shows the simulated board
            self.get_visualliser().update_board(self, simulated_map)

            return True

        return False


    def do_move(self, x1,y1,z1, x2,y2,z2, teams_turn, moved_pieces, king_class):
        '''
        params:-
            x1,y1,z1 : int : Piece to move
            x2,y2,z2 : int : Place to move to
            teams_turn : Current teams turn
            moved_pieces : Piece_subclasses : If Piece needs to have moved set
        returns:-
            bool : True if succsessfully moved, False otherwise
        '''
        if self.can_move(x1,y1,z1, x2,y2,z2, teams_turn):

            # Simulate move
            simulated_map = copy.deepcopy(self.get_map())
            simulated_map.move_piece(x1,y1,z1, x2,y2,z2)

            # Can't move if it leads to self check
            if simulated_map.is_in_check(teams_turn, king_class):
                return False

            self.move_piece(x1,y1,z1, x2,y2,z2)

            # If visualliser then update screen
            if self.get_visualliser() != False:
                self.get_visualliser().update_board(self, self.get_map())

            # If the piece is a piece that needs to track if moved
            if type(self.get_gridpoi(x2,y2,z2)) in moved_pieces:
                self.get_gridpoi(x2,y2,z2).moved = True
            
            return True

        return False


    def do_attack_board_move(self, ax1, ay1, ax2, ay2, teams_turn):

        if type(self.get_attack_gridpoi(ax1, ay1)) != AttackBoard:
            return False
        elif self.get_attack_gridpoi(ax1, ay1).team != teams_turn:
            return False
        elif type(self.get_attack_gridpoi(ax2, ay2)) != tuple:
            return False
        else:
            if self.move_attack_board(ax1, ay1, ax2, ay2) == False:
                return False

            # If visualliser then update screen
            if self.get_visualliser() != False:
                self.get_visualliser().update_board(self, self.get_map())
                
            return True

    
    # Training things
    def gamestate_str(self):
        return self.controlloop.gamestate_str(self)

    def score(self):
        bots = self.controlloop.players
        bot_scores = [0,0]

        # Messages from within game time
        for message in self.controlloop.messages:
            
            if message == bots[0] + ' is in check':
                bot_scores[0] += -2
                bot_scores[1] += 2
            elif message == bots[1] + ' is in check':
                bot_scores[0] += 2
                bot_scores[1] += -2
            elif message == bots[0] + ' is in checkmate':
                bot_scores[0] += -100
                bot_scores[1] += 100 - len(self.controlloop.history)
            elif message == bots[1] + ' is in checkmate':
                bot_scores[0] += 100 - len(self.controlloop.history)
                bot_scores[1] += -100
            elif message == 'There is over 3 repeated moves in  the past 10 history':
                bot_scores[0] += -10
                bot_scores[1] += -10
            elif message == 'Bad suggestion':
                bot_scores[0] += -10
                bot_scores[1] += -10
            elif message == 'Game lasted to long':
                bot_scores[0] += -10
                bot_scores[1] += -10

        # Board state score
        for i in range(len(bots)):

            for coords, piece in self.get_map().get_pieces_search(True, team=bots[i]):
                if type(piece) != King:
                    bot_scores[i] += piece.value

        return bot_scores
        

 

if __name__ == '__main__':
    raise RuntimeError('This code can\'t be ran due to being a class')