import streamlit as st
import pandas as pd
import pickle

st.title("Gender Classification Using Machine Learning Web App")

model = pickle.load(open('model.pkl','rb'))

st.info("Please enter the following details to get the prediction")

long_hair = st.radio("Do you have long hair?", ("No", "Yes"))
long_hair = 1 if long_hair == "Yes" else 0

forehead_width_cm = st.slider("Enter your forehead width in cm", 11.1, 15.5)

forehead_height_cm = st.slider("Enter your forehead height in cm", 5.1, 7.1)

nose_wide = st.radio("Is your nose wide?", ("No", "Yes"))
nose_wide = 1 if nose_wide == "Yes" else 0

nose_long = st.radio("Is your nose long?", ("No", "Yes"))
nose_long = 1 if nose_long == "Yes" else 0

lips_thin = st.radio("Are your lips thin?", ("No", "Yes"))
lips_thin = 1 if lips_thin == "Yes" else 0

distance_nose_to_lip_long = st.radio("Is the distance between your nose and lip long?", ("No", "Yes"))
distance_nose_to_lip_long = 1 if distance_nose_to_lip_long == "Yes" else 0

def predict():
    prediction = model.predict([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])[0]
    st.write(prediction)
    if prediction == 1:
        st.success("Male")
    else:
        st.success("Female")

st.button("Predict", on_click=predict)