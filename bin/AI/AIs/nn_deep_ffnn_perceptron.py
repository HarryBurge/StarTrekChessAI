__authour__ = 'Harry Burge'
__date_created__ = '14/07/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '14/07/2020'

# Imports
from bin.AI.ai_class import AI

import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense

class Bot(AI):

    def __init__(self, save_file=None):
        super().__init__()

        #create model
        self.model = Sequential()

        #add model layers
        self.model.add(Dense(300, activation='relu', input_shape=(240,)))
        self.model.add(Dense(200, activation='relu'))
        self.model.add(Dense(100, activation='relu'))
        self.model.add(Dense(10, activation='relu'))
        self.model.add(Dense(1))

        # self.load_weights_and_biass('bin/AI/AIs/nn_deep_ffnn_perceptron_wb/wb1.keras')
        # self.save_weights_and_biass('bin/AI/AIs/nn_deep_ffnn_perceptron_wb/wb1.keras')

        if save_file!=None:
            self.load_weights_and_biass(save_file)


    def suggest_move(self, board, team):
        moves = self.get_all_possible_moves(board, team)

        all_boards = []
        for coord1, coord2 in moves:
            all_boards.append(self.simulate_piece_move(board, *coord1, *coord2))

        heurstic_boards = []
        for simboard in all_boards:
            x_in = tf.convert_to_tensor([self.convert_map_to_float_vector(simboard, team)])
            heurstic_boards.append(float(self.model.call(x_in)))

        index_max = heurstic_boards.index(max(heurstic_boards))

        return moves[index_max][0], moves[index_max][1]

    def get_weights_and_biass(self):
        return self.model.weights

    def save_weights_and_biass(self, filepath):
        self.model.save_weights(filepath)

    def load_weights_and_biass(self, filepath):
        self.model.load_weights(filepath)
