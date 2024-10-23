import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
import twilio.rest
import cv2

# Twilio credentials
account_sid = "enter your id"
auth_token = "enter your token"
client = twilio.rest.Client(account_sid, auth_token)
c=0
b=0
# Load fire detection model
model = load_model("pages/firemodel.h5")

# Title
st.title("FIRE DETECTION APP")


# Function to preprocess image
def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((150, 150))
    img = np.array(img)
    img = img / 255.0
    return img


# Function to make prediction
def make_prediction(image):
    img = preprocess_image(image)
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    return predictions


# Upload image or use webcam
option = st.selectbox("Choose option", ["Upload image", "Use webcam"])

if option == "Upload image":
    uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        predictions = make_prediction(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", width=300)
        if predictions >= 0.5:
            st.write("SAFE")
        else:
            st.write("FIRE")
            try:
                message = client.messages.create(
                    body="FIRE",
                    from_="whatsapp:+14155238886",
                    to="whatsapp:+916235400125"
                )
                st.success("Notification sent!")
            except twilio.base.exceptions.TwilioRestException as e:
                st.error(f"Error sending notification: {e}")

elif option == "Use webcam":
    # Create placeholder
    placeholder = st.empty()

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Preprocess frame
        frame = cv2.resize(frame, (150, 150))
        frame = frame / 255.0

        # Convert frame to uint8
        frame = np.uint8(255 * frame)

        # Convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display frame
        placeholder.image(rgb_frame, channels="RGB", width=640)

        # Run frame through CNN model
        pred = model.predict(np.expand_dims(frame, axis=0))

        # Display prediction
        if pred[0][0] > 0.5:
            c=c+1
            if c==30:
               st.write('Fire detected!')
               try:
                  message = client.messages.create(
                    body="FIRE",
                    from_="whatsapp:+14155238886",
                    to="whatsapp:+916235400125"
                  )
                  st.success("Message sent!")
               except twilio.base.exceptions.TwilioRestException as e:
                st.error(f"Error sending notification: {e}")
               break
        # else:
        #     b=b+1
        #     if b==10000:
        #         c=0
        #         b=0
        #     pass

        # Limit frame rate
        import time

        time.sleep(0.05)

    # Release camera
    cap.release()
    cv2.destroyAllWindows()