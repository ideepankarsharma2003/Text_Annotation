import streamlit as st
from scripts.format_ner import format_ner_text
from scripts.get_ner_results import get_ner_results






st.title("Named Entity Recognition Results")




with st.sidebar:
    text= st.text_area("Input Text", height=30)
    btn= st.button("Perform NER")



if btn:
    # Display the original text
    st.subheader("Original Text:")
    st.write(text)

    st.subheader("NER results:")
    
    ner_results= get_ner_results(text)    
    formatted_text= format_ner_text(text, ner_results)

    # Display the formatted text with HTML
    st.write(f'''<div ">{formatted_text}</div>''', unsafe_allow_html=True)
