import streamlit as st

# dashboard

st.set_page_config(page_title = "Home",
                   page_icon = ":house:")

st.title("# Welcome to the Online Retail Dashboard! 👋")

st.header("About", divider = True)
st.write("This dashboard uses the online retail data available from  \n" + \
         "https://archive.ics.uci.edu/dataset/352/online+retail")