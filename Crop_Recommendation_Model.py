import numpy as np
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import streamlit as st
import pickle

pickle_in = open('RandomForest.pkl','rb')
RF = pickle.load(pickle_in)

st.title("CROP RECOMMEDATION WEB APP")
st.header("By Karan Kumar Singh")
N = st.number_input(label="Nitrogen level of soil",step=1,format="%i")
P = st.number_input(label="Phosphorus level of soil",step=1,format="%i")
K = st.number_input(label="Potassium level of soil",step=1,format="%i")
Temp = st.number_input(label="Temperature",step=1.,format="%.2f")
Hum = st.number_input(label="Humidity",step=1.,format="%.2f")
ph = st.number_input(label="pH Value of soil",step=1.,format="%.2f")
rnfl = st.number_input(label="Rainfall in the area",step=1.,format="%.2f")

# Data = [N,P,K,Temp,Humidity,pH,Rainfall]
data = np.array([[N, P, K, Temp, Hum, ph, rnfl]])

if st.button("Predict the crop"):
    prediction = RF.predict(data)
    st.success(f"You should cultivate {prediction[0]}.")
