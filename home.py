import streamlit as st
import pandas as pd

st.title("❤️❤️Website Developing using Python❤️❤️")
st.header("🚗🚗Website Developing using Python🚗🚗")

st.image('./img/323283346_5718974981503456_3654895059501341451_n.jpg')
st.subheader("Aphichat ")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))


