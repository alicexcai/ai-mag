# ai-mag
the first AI literary magazine

### setup
0. create webapp/.env and add OPENAI_API_KEY=enter your api key
1. pip install -r requirements.txt
2. cd webapp
3. python -m streamlit run ABOUT.py

### logs

**setup**
* frontend
* connection to advo org
* data processor - generate fine-tune csv, format few-shot prompt
* dynamic config for few-shot formatting

**notes on manual data processing**
* removed special eol characters on vscode prompt
* removed the-sea-beyond-this-world.txt
* removed the-female-voice.txt
* replaced special characters "&nbsp\;" and "\xa0" with spaces