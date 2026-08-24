import streamlit as st
#title
st.title("ML project Documentation")
#header/subheader
st.header("This is header")
st.subheader("This is subheader")
#text
st.text("This is text")
#markdown
st.markdown("# This is header-1")
st.markdown("## This is header-2")
st.markdown("### This is header-3")
#error/colorful text
st.error("This is error message")
st.warning("This is warning message")
st.success("This is success message")
st.info("This is info message")
#exception
st.exception("NameError('Name pd not defined')")

import math
st.help(math.pow)
st.help(print)
#using write
st.write("This is write function")
#importing audio,image and video files
#PIL- Python Imaging Library
from PIL import Image
img=Image.open("plot1.png")
st.image(img,width=300,caption="Sinusoidal Wave")
st.audio("Tune1.aac")
st.video("rain.mp4")

