import streamlit as st
from tqdm import tqdm
from uuid import uuid4
import os
from scripts.image_gen import gen_image
from PIL import Image
import shutil


with st.sidebar:
    tb= st.text_area(label="Enter image links...")
    btn= st.button(label="Gen Image")
if btn:
    links= tb.split('\n')
    st.write(links)
    
    project_uid= uuid4().hex.__str__()
    print(f"project_uid: {project_uid}")
    os.makedirs(f"media/{project_uid}", exist_ok=True)
    
    for link in tqdm(links):
        basename= os.path.basename(link)
        print(basename)
        gen_image(link, project_uid)
        img= Image.open(f"media/{project_uid}/{basename}")
        col1, col2= st.columns(2)
        with col1:
            st.image(link, caption="original", use_column_width=True)
        with col2:
            st.image(img, caption="generated", use_column_width=True)
        # st.image([link, img], width=250, caption=["original", "generated"])
        
    shutil.rmtree(f"media/{project_uid}", ignore_errors=True)
        
        
    
    
    
    
