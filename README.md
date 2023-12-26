# visual-search_PINECONE
PineCone VectorSearch Implementation
```
v1.0: Generic image search implementation. 
v2.0: Prototyping an accessory customizer via the Dall-E API.
v3.0: PineCone vector implementation to speed up search (faster retrieval in larger databases). 
```
This is a Streamlit web page that showcases a comparison between L2-Distance Search and Vectorize Search methods. The page contains two columns where the first column displays some markdown text and a link to a GitHub repository, while the second column displays an animation loaded from a JSON file. Additionally, the page includes an expander widget that compares the two types of search methods.

- Libraries Used
The following libraries have been used in this Streamlit app:

streamlit: for creating web pages
streamlit_lottie: for adding animations
json: for working with JSON files
Page Configuration
The set_page_config function from the streamlit library has been used to set the page configuration. The page_title parameter has been set to "Home".

- Columns
Two columns have been created for the page using the columns function from the streamlit library. The cols1 and cols2 variables represent the two columns.

- First Column
The first column (cols1) displays some markdown text and a link to a GitHub repository. The markdown text contains a message asking the user to select a task from the sidebar, and the link leads to the GitHub repository for Assignment-4.

- Second Column
The second column (cols2) displays an animation loaded from a JSON file. The animation is displayed using the st_lottie function from the streamlit_lottie library. The JSON file contains the animation data.

- Expander Widget
An expander widget has been added to the page using the expander function from the streamlit library. The widget compares L2-Distance Search and Vectorize Search methods, highlighting the differences between them. The comparison is presented in a table format.

- Web Application for Image Search
This code implements a web application for image search using Elastic Search. The user can upload an image and the application will recommend similar images based on the L2 distance between the uploaded image and the images already present in the system. The recommended images are displayed in a grid format based on the number of columns and rows selected by the user.

- Libraries
pandas - For data manipulation and analysis
streamlit - For creating web pages
PIL - For working with images
pathlib - For working with file paths
numpy - For numerical computing
feature_extractor - A custom module for extracting features from images
datetime - For working with dates and times
- Functions
sis_offline() - A function that takes an image file as input, extracts features from it, computes L2 distances between the uploaded image and the images already present in the system, and recommends similar images based on the number of recommendations and the grid size selected by the user.

- Usage
The user can upload an image by clicking on the "Choose an Image file" button.
Once the image is uploaded, it is displayed on the page along with its extracted features.
The user can select the number of recommendations and the grid size using sliders and number inputs.
The recommended images are displayed in a grid format based on the selected grid size.
