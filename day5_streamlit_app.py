import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.write")

# Example 1. Includes the usage of markdown to put text into italics and
# emojis

st.write("Hello, *World!* :sunglasses:")

# Example 2. Prints numbers in markdown format.

st.write(1234)

# Example 3. Print out of Pandas DataFrame as a table. When using

df = pd.DataFrame({"first column": list(range(0, 5, 1)),
                   "second column": list(range(0, 100, 20))})
st.write(df)

# Example 4. Here the Pandas DataFrame is printed on a new line.

st.write("Below is a DataFrame:", df, "Above is a dataframe.")

# Example 5. Plotting a chart using st.write()

df2 = pd.DataFrame(np.random.randn(200, 3),
                   columns = ["a", "b", "c"])
c = alt.Chart(df2).mark_circle().encode(x = "a",
                                        y = "b",
                                        size = "c",
                                        color = "c",
                                        tooltip = ["a", "b", "c"])
st.write(c)

# Example 6. Using st.markdown
st.write("st.write()")
st.markdown("st.markdown(*body*, help != None)",
            help = "This is the markdown help option that can be included")
st.header("st.header(*body*, divider = True, help != None)",
          divider = True,
          help = "This is the header help option that can be included")
st.subheader("st.subheader(*body*, divider = True, help != None)",
          divider = True,
          help = "This is the subheader help option that can be included")