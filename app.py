import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content




# You can access the image with PIL.Image for example
import io
from PIL import Image
from ai import recommend_food
from recommendation_functions import name_of_food,recipe_of_food,recommend_similar_food_func


LLM,RFR=st.tabs(["Talk to LLM","Recommendations From Recommender"])





with LLM:
    prompt = st.chat_input("What do you want to eat")
    if prompt:
        
        with st.chat_message("user"):
            st.write(f"{prompt}")
            try:
                recommend_food(prompt)
                image_bytes = query({"inputs": f"{name_of_food()}",})                      
                image = Image.open(io.BytesIO(image_bytes))
            except Exception as e:
                if 'JSONDecodeError' in str(e):
                    recommend_food(prompt)
                    image_bytes = query({"inputs": f"{name_of_food()}",})                      
                    image = Image.open(io.BytesIO(image_bytes))
                else:st.write(e)
        with st.chat_message("Assistant"):
            try:
                st.write(name_of_food())
                st.image(image)
                st.write(recipe_of_food())
            except Exception as e:
                    if 'JSONDecodeError' in e:
                        st.write(name_of_food())
                        st.image(image)
                        st.write(recipe_of_food())
                    else:st.write(e)
                        
            
                    
with RFR:
     if prompt:
          st.write(recommend_similar_food_func())
          
     
                
        







