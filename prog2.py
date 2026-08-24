import streamlit as st
#title
st.title("Streamlit text imputs examples...")
#text input
name=st.text_input("Enter your name:")
#text area
feedback=st.text_area("Enter your feedback:")
#number input
age=st.number_input("Enter your age:",min_value=0,max_value=120,step=5)
#date input
date=st.date_input("Enter your date:")
#time input
time=st.time_input("Enter your time:")
#color picker
color=st.color_picker("Pick your favorite color:")
#dislpay the inputs
st.write("Name:",name)
st.write("Feedback:",feedback)
st.write("Age:",age)
st.write("Date:",date)
st.write("Time:",time)
st.write("Color:",color)

