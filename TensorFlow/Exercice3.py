##################################
#
# Tutorials #3 for Tensorflow
#
##################################

# future lib import
from __future__ import absolute_import, division, print_function

# Tensorflow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# Boston housing prices dataset
def Regression():
    boston_housing = keras.datasets.boston_housing

    (train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

    # Shuffle the training set
    order = np.argsort(np.random.random(train_labels.shape))
    train_data = train_data[order]
    train_labels = train_labels[order]

    print("Training set: {}".format(train_data.shape))  # 404 examples, 13 features
    print("Testing set:  {}".format(test_data.shape))   # 102 examples, 13 features





