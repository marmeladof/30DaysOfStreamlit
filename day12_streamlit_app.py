import streamlit as st

st.header("st.checkbox")

st.write("What would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more :ice_cream:")

if coffee:
    st.write("Okay, here's some :coffee: for you")

if cola:
    st.write("Bring on the fizz! :cup_with_straw:")