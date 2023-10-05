import streamlit as st

st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there!")
    st.write("If you'd like to say goodbye, click the button below")
else:
    st.write("")

if st.button("Say goodbye"):
    st.write("Goodbye!")
    st.write("If you'd like to say hello, click the button above")
else:
    st.write("")