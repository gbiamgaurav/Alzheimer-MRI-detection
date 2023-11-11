import os
import streamlit as st
from io import BytesIO
import base64
from PIL import Image
from alzeihmer_detection.utils import decodeImage
from alzeihmer_detection.pipeline.predictions import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

st.title("Alzeihmer Disease Prediction")

page = st.selectbox("Select a page:", ["Home", "Predict"])

if page == "Home":
    st.header("Home Page")
    st.write("Welcome to the Alzeihmer Disease Prediction App")
    st.write("You can use the navigation bar on the left to access different pages")

elif page == "Predict":
    st.header("Predict Page")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        try:
            # Open the image using Pillow
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Encode the image as bytes
            with BytesIO() as buffer:
                image.save(buffer, format="JPEG")
                image_bytes = buffer.getvalue()

            if st.button("Predict"):
                # Pass the base64-encoded image data to the decodeImage function
                decodeImage(base64.b64encode(image_bytes), clApp.filename)
                result = clApp.classifier.predict()

                # Display the prediction result in a single line
                if result:
                    st.write(f"Prediction Result is: {result[0]['image']}")

        except Exception as e:
            st.error(f"Error: {str(e)}")
