"""
generate.py stores methods to generate text and images using ai
"""
from . import classes

import requests
import openai
import os

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-Ox6aCGz8gQrZEsxvCX0LeGh6"

import yaml
with open(os.getcwd() + "utils/config.yml") as f:
    configData = yaml.safe_load(f)

# PROCESS

def process_data(writing_type):
    examples = classes.WritingData(writing_type).examples
    return examples

# GENERATE

def get_completion(prompt, model):

    completion = openai.Completion.create(
        engine = model,
        temperature = 0.7,
        max_tokens = 200,
        prompt = prompt,
        frequency_penalty = 1.0,
        stop = ["###"]
        ).choices[0].text.rstrip()

    return completion

def generate_text_fewshot(topic, examples, writing_type, model):

    # examples = classes.WritingData(writing_type).examples
    promptInstance = classes.Prompt(examples, configData["promptTemplates"][writing_type])
    prompt = promptInstance.composeCurrentPrompt(topic)
    completion = get_completion(prompt, model)
    
    return completion

def generate_text_finetuned(topic, model):

    completion = get_completion(topic, model)
    
    return completion

# FETCH MODELS

def fetch_finetunes():
    
    fine_tunes = openai.FineTune.list()
    fine_tunes_list = []
    for i in range(len(fine_tunes['data'])):
        fine_tunes_list.append(fine_tunes['data'][i]['fine_tuned_model'])
    fine_tunes_list = [ft for ft in fine_tunes_list if ft]
    return fine_tunes_list

def fetch_engines():
    
    engines = openai.Engine.list()
    engine_list = []
    for i in range(len(engines['data'])):
        engine_list.append(engines['data'][i]['id'])
    return engine_list

# def fetch_all_models():

#     models = fetch_engines() + fetch_finetunes()
#     return models
