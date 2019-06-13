import pandas as pd
import numpy as np
import re, os, pprint

# global variable
pprint = pprint.pprint

DATASETS = "datasets/"

def load_Data(path=DATASETS):
    data = []
    txt_path = os.path.join(path, "Mark.txt")
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
    data = smooth_Data(data)
    print(data)
    

if __name__ == "__main__":
    main()