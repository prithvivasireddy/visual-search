# Importing libraries
import streamlit as st  # Streamlit library for creating web pages
from streamlit_lottie import st_lottie  # Streamlit Lottie library for adding animations
import json  # Library for working with JSON files

# Set page configuration
st.set_page_config(
    page_title="Home",  # Title of the page
)

# Create title for the page
st.title("Image Search")

# Create two columns for the page
cols1,cols2=st.columns(2)

# Populate first column with markdown text and link to GitHub repository
with cols1:
    st.markdown(
        """
        **👈 Select Task from the sidebar** 
        ### Visit the github repository 
        - [Assignment -4 : Github](https://github.com/Negi97Mohit/Digital_Marketing.git)
       """
    )

# Populate second column with an animation loaded from a JSON file
with cols2:    
        path = "99274-loading.json"
        with open(path,"r") as file:
            url = json.load(file)
            st_lottie(url,
            reverse=True,
            height=450,
            width=450,
            speed=1,
            loop=True,
            quality='high',
            key='Car'
        )

# Create an expander widget that compares two types of search methods
with st.expander("Elastic Search Vs Vector Search : Comparison"):
    st.markdown("""
    | L2 - Distance Search                                                                        | Vectorize Search                               |
|---------------------------------------------------------------------------------------------|------------------------------------------------|
| Lower processing speed                                                                      | Faster processing speed                        |
| Less preprocessing required                                                                 | Vectorization of dataset required              |
| Cannot be used for text based data                                                          | Works with both text and image based data      |
| Search parameters limited                                                                   | Filtering can be used for meta data            |
| Runs locally and uses CPU for processing can use GPUs for preprocessing but not for quering | Computes on cloud and can use GPU for quering  |
    """)
