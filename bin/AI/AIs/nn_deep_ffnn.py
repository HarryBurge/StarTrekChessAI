__authour__ = 'Harry Burge'
__date_created__ = '14/07/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '14/07/2020'

# Imports
from bin.AI.ai_class import AI
import tensorflow.compat.v1 as tf
import numpy as np
import copy
tf.disable_v2_behavior()


class Bot(AI):

    def __init__(self):
        super().__init__()

        # Reset the graph
        tf.reset_default_graph()

        # input x - for 6 x 10 x 4 = 240
        self.X = tf.placeholder(tf.float32, [None, 240], name='X')

        # x to hidden layer 1
        W1 = tf.Variable(tf.random_normal([240, 300], stddev=0.03), name='W1')
        b1 = tf.Variable(tf.random_normal([300]), name='b1')

        # hidden layer 1 to 2
        W2 = tf.Variable(tf.random_normal([300, 270], stddev=0.03), name='W2')
        b2 = tf.Variable(tf.random_normal([270]), name='b2')

        # hidden layer 2 to y
        W3 = tf.Variable(tf.random_normal([270, 240], stddev=0.03), name='W3')
        b3 = tf.Variable(tf.random_normal([240]), name='b3')

        # calculate the output of the hidden layer
        hidden1_out = tf.add(tf.matmul(self.X, W1), b1)
        hidden1_out = tf.sigmoid(hidden1_out)

        # calculate the output of the hidden layer
        hidden2_out = tf.add(tf.matmul(hidden1_out, W2), b2)
        hidden2_out = tf.sigmoid(hidden2_out)

        # Our output layer
        y_est = tf.nn.softmax(tf.add(tf.matmul(hidden2_out, W3), b3))
        self.y_est_clipped = tf.clip_by_value(y_est, 1e-10, 0.9999999)

        # Initialize variables and run session
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)


    def suggest_move(self, board, team):

        def bound_of_array_split(arr_size, split_into, index):
            chunks_size = arr_size // split_into

            counter = 0
            bounds_top = chunks_size

            while index >= bounds_top:
                bounds_top += chunks_size
                counter += 1

            return counter

        input_x = self.convert_map_to_float_vector(board, team)
        y_out = self.sess.run(self.y_est_clipped, feed_dict={self.X: [input_x]})

        y_tops = np.argsort(y_out)[0][:2]

        # Translate y_tops index vals to coord points
        xl, yl, zl = board._size

        coords = []

        for val in y_tops:
            z = bound_of_array_split(len(y_out[0]), zl, val)
            bound = np.array_split(y_out[0], zl)[z]

            neg = z*len(bound)

            y = bound_of_array_split(len(bound), yl, val-neg)
            bound = np.array_split(bound, yl)[y]

            neg += y*len(bound)
            x = val - neg

            coords.append((x,y,z))

        return coords[0], coords[1]