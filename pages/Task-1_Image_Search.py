# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:11:43 2023

This code appears to be an implementation of a web application for image search.

"""

# Importing libraries
import pandas as pd

# Dashboard and Report libraries
import streamlit as st

# Importing from the sis offline.py
from PIL import Image
from pathlib import Path
import numpy as np
import feature_extractor
from datetime import datetime

st.set_page_config(layout="wide")

# Setting up the main page and sidebar
st.markdown("# Elastic Search")
st.sidebar.header("Elastic Search")

# Function from sis offline.py
def sis_offline():

    # Uploading a file
    uploaded_file = st.file_uploader("Choose an Image file")
    
    if uploaded_file is not None:
        
        uploaded_path = uploaded_file.name
        features = []
        img_paths = []
        
        # Loading features and image paths from files saved on disk
        for feature_path in Path("./static/feature").glob("*.npy"):
            features.append(np.load(feature_path))
            img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
        features = np.array(features)

        # Saving the uploaded file and displaying it on the page
        img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + str(uploaded_path)
        with open(img_path, "wb") as f:
            f.write(uploaded_file.getbuffer())  # e.g., ./static/img/xxx.jpg
        up_img = Image.open(img_path)
        up_img = up_img.resize((400, 600))
        st.image(up_img)

        # Extracting features from the uploaded file
        uploaded_feature = feature_extractor.extract(img=Image.open(img_path))
        st.write(uploaded_feature)

        # Setting the number of recommended images to be displayed and computing the L2 distance between uploaded file and system files
        age = st.slider('How many recommendations', 0, 50, 10)
        dists = np.linalg.norm(features-uploaded_feature, axis=1)  # L2 distances to features
        ids = np.argsort(dists)[1:age+1]  # Top 30 results
        scores = [(dists[id], img_paths[id]) for id in ids]
        
        #Grid Setting for iages
        n_cols=int(st.number_input("Grid Size",2,8,4))
        n_pics=len(scores)
        n_rows=int(1+n_pics//n_cols)
        rows=[st.columns(n_cols) for  _ in range(n_rows)]
        cols=[column for row in rows for column in row]

        for col,image_url in zip(cols,scores):
            image = Image.open(image_url[1])
            image = image.resize((400, 600))
            col.image(image)   
    else:
        st.write("Upload File")

# Function call for EDA
if __name__ == "__main__":
    sis_offline()
