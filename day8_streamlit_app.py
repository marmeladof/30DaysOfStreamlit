import streamlit as st
from datetime import time, datetime

st.header("st.slider")

# Example 1. Creating a slider with different values.
# The parameters given are the start, the end, and the default value.

st.subheader("Slider")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm", age, "years old")

# Example 2. st.slider() can be used to define a range

st.subheader("Range slider")

values = st.slider("Select a range of values",
                   0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

# Example 3. The values used by a slider can also be datetime formats, not just numerical values

st.subheader("Range time slider")

appointment = st.slider("Schedule your appointment:",
                        value = (time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4. Here the slider takes the default value, and sets
# default range to the value (in this case 14 days ahead and before)

st.subheader("Datetime slider")

start_time = st.slider("When do you start?",
                       value = datetime(2020, 1, 1, 9, 30),
                       format = "DD/MM/YY - hh:mm")
st.write("Start time:", start_time)