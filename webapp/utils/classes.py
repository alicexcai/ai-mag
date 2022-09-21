import os
import csv

class Params:
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class WritingExample:
        
        def __init__(self, topic, content):
            self.topic = topic
            self.content = content
            self.summary = ""

class WritingData:

    def __init__(self, writing_type):
        self.writing_type = writing_type
        self.examples = self.load_examples()
        self.csv_file = self.save_data()
    
    def load_examples(self):
        examples_dict = {}
        directory = os.getcwd() + "/webapp/data/" + self.writing_type
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                with open(directory + "/" + filename, 'r', encoding='utf-8') as f:
                    rcontent = f.readlines()
                    content = ''.join(rcontent).replace("&nbsp;", " ").replace("\xa0", " ")
                topic = filename.replace("-", " ").replace(".txt", "")
                examples_dict[filename] = WritingExample(content=content, topic=topic)
        self.examples = examples_dict
        return self.examples


    def save_data(self):
        self.dataPath = os.getcwd() + "/webapp/data/" + self.writing_type + "/data.csv"
        with open(self.dataPath, 'w') as csv_file:  
            writer = csv.writer(csv_file)
            writer.writerow(["prompt", "completion"])
            for filename, example in self.examples.items():
                writer.writerow([example.topic, example.content])

        return self.dataPath

class Prompt:

    def __init__(self, examples, template, numExamples=3): # examples is a list of examples
        self.numExamples = numExamples
        self.examples = examples # {"example": "example", "topic": "topic"}
        self.template = template # {"variables": ["var1", "var2"], "template": "template"}
        self.promptBase = self.composePromptBase()
        self.currentPrompt = None
        
    def composePromptBase(self):
        self.promptBase = ""
        for example in list(self.examples.items())[:self.numExamples]:
            promptSegment = self.template["template"].format_map({"topic": example[1].topic, "example": example[1].content})
            self.promptBase += promptSegment
        return self.promptBase

    def composeCurrentPrompt(self, topic):
        self.currentPrompt = self.promptBase + self.template["prefix"].format_map({"topic": topic})

        return self.currentPrompt
    