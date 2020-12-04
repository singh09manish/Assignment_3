import streamlit as st
import json
import requests


menu = ["Home", "Analysis"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
     st.subheader("Welcome To sentiment analysis web App")

elif choice == "Analysis":
    st.subheader("Put your input here")

    username = st.text_input("Input")






