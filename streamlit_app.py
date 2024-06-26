
# Web App using streamlit

import streamlit as st
# Load the model and scaler instances
import pickle
import numpy as np

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('minmaxscaler.pkl', 'rb') as minmaxscaler_file:
    minmaxscaler = pickle.load(minmaxscaler_file)

with open('standscaler.pkl', 'rb') as standscaler_file:
    standscaler = pickle.load(standscaler_file)

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About Project"])

# Main Page
if app_mode == "Home":
    st.markdown("<h2 style='text-align: center; color: white;'>CROP PREDICTION USING SOIL ANALYSIS </h2>", unsafe_allow_html=True)
    st.image("banner.png")
    st.subheader('Required Values', divider='rainbow')
    n = st.number_input("Nitrogen:", min_value=0,max_value=150,step=1)
    p = st.number_input("Phosphorus:", min_value=0,max_value=150, step=1)
    k = st.number_input("Potassium:", min_value=0,max_value=210, step=1)
    temp = st.number_input("Temperature:", min_value=0,max_value=50,step=1)
    hum = st.number_input("Humidity:",min_value=0,max_value=100, step=1)
    ph = st.number_input("pH:",min_value=0,max_value=14,step=1)
    rain = st.number_input("Rainfall:",min_value=0,max_value=350,step=1)

    # Button for prediction
    if st.button("Predict"):
        # Process user input
        input_data = np.array([[n, p, k, temp, hum, ph, rain]])
        input_data_scaled = minmaxscaler.transform(input_data)
        input_data_scaled = standscaler.transform(input_data_scaled)
        #st.write("Input data:", input_data)  # Debugging statement

        
         
        # Make predictions
        prediction = model.predict(input_data_scaled)

        # Display results
        crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                     8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                     14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                     19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            st.write("{} is a best crop to be cultivated ".format(crop))
        else:
            st.write("Sorry are not able to recommend a proper crop for this environment")
if app_mode == "About Project":
    st.header("About Project",divider="red")
    st.subheader("About Dataset",divider='blue')
    st.write("This dataset was build by augmenting datasets of rainfall, climate and fertilizer data available for India.")
    st.markdown("##### Data fields")
    st.markdown("* N - ratio of Nitrogen content in soil")
    st.markdown("* P - ratio of Phosphorous content in soil")
    st.markdown("* K - ratio of Potassium content in soil")
    st.markdown("* temperature - temperature in degree Celsius")
    st.markdown("* humidity - relative humidity in %")
    st.markdown("* ph - ph value of the soil")
    st.markdown("* rainfall - rainfall in mm")
    st.text("Dataset taken from:")
    st.code("https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset")
    st.subheader("Project Objective",divider='blue')
    st.write("Maximize agricultural yield by recommending appropriate crops")

