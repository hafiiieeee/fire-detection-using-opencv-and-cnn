import streamlit as st
import pickle
from PIL import Image
import base64
def get_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

image = get_image("backbg.jpg")
url="https://colab.research.google.com/drive/1Ayb6vN7SBhyiLm2WL7bT-xjvTb6eUTpM"
url2="https://www.kaggle.com/datasets/brsdincer/wildfire-detection-image-data"
def home():
    st.markdown(
        f"""<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>""", unsafe_allow_html=True
    )
    new_title = '<p style="font-family:sans-serif; font-size: 48px; ">Fire Detection App: Protecting Lives and Property</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    new_title = '<p style="font-family:sans-serif; font-size: 20px;">WELCOME!</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('''
        In the event of a fire, every second counts. Traditional fire detection systems can be unreliable, slow, and ineffective. Our Fire Detection App leverages cutting-edge AI technology to detect fires quickly and accurately, providing crucial seconds for evacuation and emergency response.
        ''')

    new_title = '<p style="font-family:sans-serif; font-size: 25px;">About Our App</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('''
        
Our app utilizes a  convolutional neural network and deep learning-based approach to detect fires from images and video streams. With real-time notifications and alerts, our system ensures prompt action can be taken to prevent catastrophic damage.
        ''')

    new_title = '<p style="font-family:sans-serif; font-size: 25px;">Key Features</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown('''
        - Real-time fire detection from images and video streams
        - AI-powered accuracy for reliable detection
        - Instant notifications and alerts for emergency response
        - User-friendly interface for easy monitoring
        ''')

    new_title = '<p style="font-family:sans-serif; ; font-size: 25px;">Stay Safe, Stay Protected</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown("""
            This introduction provides a concise overview of the app's purpose, features, and benefits. You can customize it to fit your project's specific needs and design.
            """)
    st.write("GOOGLE COLAB:[FIRE DETECTION](%s)" % url)
    st.write("DATASET:[Wildfire Detection Image Data](%s)" % url2)

home()