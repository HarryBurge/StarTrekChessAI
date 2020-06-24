__authour__ = 'Harry Burge'
__date_created__ = '20/06/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '20/06/2020'

# Imports
import importlib


class AI_Controller:

    def __init__(self, ai_path, backtest=False):
        self.AI = importlib.import_module(ai_path).Bot()


    def get_AI(self):
        return self.AI


    def suggest_move(self, board, team):
        return self.get_AI().suggest_move(board, team)