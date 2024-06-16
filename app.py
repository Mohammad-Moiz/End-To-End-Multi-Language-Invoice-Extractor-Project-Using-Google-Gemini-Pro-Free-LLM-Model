from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from prompt import input_prompt
from get_gemini_response import get_gemini_response
from input_image_details import input_image_details

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

##initialize our streamlit app
st.set_page_config(page_title="MultiLanguage Invoice Extractor")

st.header("MultiLanguage Invoice Extractor")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

## if submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Rresponse is")
    st.write(response)