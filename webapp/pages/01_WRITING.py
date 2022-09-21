import streamlit as st
import utils.generate

st.title("WRITING")

writing_type = st.selectbox("Writing Type", ["poetry", "fiction", "non-fiction"])

col1, col2 = st.columns(2)
generation_type = col1.selectbox("Generation Type", ["Fine-tuned", "Few-shot"])
if generation_type == "Fine-tuned":
    fine_tunes_list = utils.generate.fetch_finetunes()
    model = col2.selectbox("Fine-tuned Model", fine_tunes_list)
else:
    engines_list = utils.generate.fetch_engines()
    model = col2.selectbox("Few-shot Engines", engines_list)

topic = st.text_input("Topic of your piece")
if st.button("Generate"):
    with st.spinner("Generating..."):
        examples = utils.generate.process_data(writing_type)
        if generation_type == "Fine-tuned":
            output = utils.generate.generate_text_finetuned(topic=topic, model=model)
            st.write(output)
        else:
            output = utils.generate.generate_text_fewshot(topic=topic, examples=examples, writing_type=writing_type, model=model)
            st.write(output)
        st.success("Done!")

# # TEMP

# import csv
# import os
# if st.button("Process data"):
#     with open(os.getcwd() + '/data/poetry/dict.csv', 'w') as csv_file:  
#         writer = csv.writer(csv_file)
#         for key, value in mydict.items():
#             writer.writerow([key, value])