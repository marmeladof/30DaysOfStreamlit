import streamlit as st

st.header("st.selectbox")

option = st.selectbox("What is your favourite colour?",
                      ("Blue", "Red", "Green"))

st.write("Your favourite colour is ", option)