
# Web App using streamlit

import streamlit as st

#Sidebar

st.sidebar.title("Dashboard")
app_mode= st.sidebar.selectbox("Seletct Page",["Home","About Project"])


#Main Page
if(app_mode=="Home"):
    st.markdown("<h2 style='text-align: center; color: white;'>CROP PREDICTION USING SOIL ANALYSIS </h2>", unsafe_allow_html=True)
    st.image("Screenshot 2024-02-22 204925.png")
    st.subheader('Required Values', divider='rainbow')
    n=st.number_input("Nitrogen:",step=1)
    st.write(n)
    p=st.number_input("Phosphorus:",step=1)
    st.write(p)
    k=st.number_input("Pottasium:",step=1)
    st.write(k)
    temp=st.number_input("Temperature:")
    st.write(temp)
    ph=st.number_input("PH:")
    st.write(ph)
    rain=st.number_input("Rainfall:")
    st.write(rain)
