#########################################################
#
# Installing Python and OpenCV for python
# Go to  C:\Users\usager\AppData\Local\Programs\Python\Python36\Scripts>
# 
# To install Python :  C:\Users\usager\AppData\Local\Programs\Python\Python36\Scripts> pip3 install --upgrade tensorflow
# To install opencv :  C:\Users\usager\AppData\Local\Programs\Python\Python36\Scripts> pip3 install opencv-python
#
#########################################################

import tensorflow as tf
import numpy as np
import sys
import cv2
import time

import Helper as Hlp
import NotesDeCours as NC
import Exercice1 as e1
import Exercice2 as e2
import Exercice3 as e3
#import TensorBoard as TB

#########################################################
#
# Main body
#
#########################################################

#e1.Classification()
#e2.TextClassification()
e3.Regression()
#NC.EspaceReserve()
#NC.Variable()
#NC.Matrice()
#NC.MultiNode();
#NC.BaseGraphe(4,3)

