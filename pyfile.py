import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


st.title("This is TITLE")
st.markdown("This is MARKDOWN")
st.header("This is HEADER")
st.subheader("This is SUBHEADER")
st.code("This is code chunk")
st.latex(r''' a = e^3 + \alpha_i + \beta_j''')

image = Image.open(r"D:\Dropbox\wave\projects\streamlit\anim0614.jpg")
st.image(image)

y = np.random.rand(30)
x = range(0, 30, 1)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

## for side bar
st.sidebar.slider("Bar", 0, 100)
st.sidebar.number_input("Enter a Number", 0, 100)