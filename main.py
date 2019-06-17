from __future__ import absolute_import, division, print_function

import argparse
import collections
import math
import os, sys, re
import random
from tempfile import gettempdir
import zipfile

import pandas as pd
import numpy as np
import pprint

from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin

import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector

data_index = 0

# global variable
pprint = pprint.pprint

DATASETS = "datasets/"

def load_Data(path=DATASETS):
    data = []
    txt_path = os.path.join(path, "Notify.txt")
    file = open(txt_path, "r").readlines()
    for line in file:
        data.append(line)
    return data

def remove_link_email(text):
    text = re.sub(r'\S*@\S*\s?', '', text, flags=re.MULTILINE) # remove email
    text = re.sub(r'http\S+', '', text, flags=re.MULTILINE) # remove web addresses
    return text

def remove_newline(text):
    return text.rstrip()

def remove_punctuation(text):
    '''a function for removing punctuation'''
    import string
    # replacing the punctuations with no space, 
    # which in effect deletes the punctuation marks 
    translator = str.maketrans('', '', string.punctuation)
    # return the text stripped of punctuation marks
    return text.translate(translator)

def smooth_Data(data):
    data['text'] = data['text'].apply(remove_newline)
    data['text'] = data['text'].apply(remove_punctuation)
    return data

def main():
    df = load_Data()
    train_data = df[:10]
    data = pd.DataFrame(train_data, columns = ['text'])
    print(data)
    data = smooth_Data(data)
    print(data)
    

if __name__ == "__main__":
    #tf.app.run()
    main()