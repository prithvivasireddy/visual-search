# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:11:43 2023
@author: mohit
"""

#Importing streamlit
import pandas as pd
import numpy as np
import os
from pathlib import Path

import streamlit as st
import pinecone
import numpy as np
from PIL import Image

from torchvision import transforms as ts 
import torchvision.models as models

st.set_page_config(layout="wide")
st.sidebar.header("Vectorized Search")


#vector generating class
class ImageEmbedder:
    def __init__(self):
        self.normalize=ts.Normalize(
            mean=[0.485,0.456,0.406],std=[0.229,0.224,0.225]
        )
        self.model=models.squeezenet1_0(pretrained=True,progress=False)

    def embed(self,image_file_name):
        image=Image.open(image_file_name)
        image=ts.Resize(256)(image)
        image=ts.CenterCrop(224)(image)
        tensor=ts.ToTensor()(image)
        tensor=self.normalize(tensor).reshape(1,3,224,224)
        vector=self.model(tensor).cpu().detach().numpy().flatten().tolist()
        return vector



#main code
st.title("PINECONE - Vector Search")

def main():  
    global stemvaler
    imgs_url=[]
    pinecone.init('18688bbc-9aa5-4be2-a87d-29c18cede436',environment='us-west4-gcp')
    INDEX_NAME='img-vector'
    index=pinecone.Index(INDEX_NAME)
    cols1,cols2=st.columns(2)
    with cols1:  
        image_count = st.slider('How many recommendations', 0, 50, 10)
        gender_val=st.radio('Select the Gender',('MEN','WOMEN'),horizontal=True)
        men_Department = st.selectbox(
            'Select Men Dept',
            ['Jackets_Vests','Pants','Shirts_Polos','Suiting','Sweaters'])
        women_Department = st.selectbox(
            'Select Women Dept',
            ['Cardigans','Dresses','Jackets_Coats','Pants','Sweaters'])
        
    with cols2:
        image_embedder = ImageEmbedder()
        uploaded_file = st.file_uploader("Choose a Image file")
        if uploaded_file is not None:
            st.image(uploaded_file, channels="BGR")
            uploaded_path=uploaded_file.name

            #Load image data and save the image
            img_path=Path("./static/uploaded")/Path(Path(uploaded_file.name).stem+".jpg")
            with open(img_path,"wb") as f:
                f.write(uploaded_file.getbuffer())  # e.g., ./static/img/xxx.jpg
            vectors=image_embedder.embed(img_path)
            if gender_val=='WOMEN':
                output=index.query(vectors,filter={
                    'gender':'women',
                    'dept':women_Department
                },top_k=image_count)
            else:
                output=index.query(vectors,filter={
                    'gender':'men',
                    'dept':men_Department
                },top_k=image_count)
            
            match=output.get('matches')                
            for mat in match:
                impath=mat.get('id')
                stemval=Path(impath).stem
                stemvaler=stemval              
                if stemvaler not in uploaded_path:
                    web_im='https://raw.githubusercontent.com/Negi97Mohit/dm_imgs/main/'+impath
                    imgs_url.append(web_im)   
                else:
                    print('Return')
        else:
            st.write("Upload an image")
    #Grid Setting for iages
    n_cols=int(st.number_input("Grid Size",2,8,4))
    n_pics=len(imgs_url)
    n_rows=int(1+n_pics//n_cols)
    rows=[st.columns(n_cols) for  _ in range(n_rows)]
    cols=[column for row in rows for column in row]

    for col,image_url in zip(cols,imgs_url):
        col.image(image_url)   

#function for EDA
if __name__ == "__main__":
    main()




