from collections import defaultdict
import os

def load_examples(writing_type):
    examples_dict = defaultdict()
    directory = os.getcwd() + "/webapp/data/" + writing_type
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(directory + "/" + filename, 'r', encoding='utf-8') as f:
                content = f.readlines()
            examples_dict[filename] = ''.join(content).replace("&nbsp;", " ").replace("\xa0", " ")

    return examples_dict
