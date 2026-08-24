import streamlit as st
#button
if st.button("Click me"):
    st.write("Button clicked!")
else:
    st.write("Button not clicked!")
#checkbox
checkbox_state = st.checkbox("Check me to enable choice")
if (checkbox_state):
    st.write("Choice enabled!")
else:
    st.write("Choice disabled!")
#radio button
radio_selection = st.radio("Select an option:", ["NLP", "ML", "DL","LangChain","Gen-AI"])
st.write("Your selection:", radio_selection)
#selectbox
selectbox_selection = st.selectbox("Select an Item:", ["NLP", "ML", "DL","LangChain","Gen-AI"])
st.write("Your selection:", selectbox_selection)
#multiselect
multiselect_selection = st.multiselect("Select multiple items:", ["NLP", "ML", "DL","LangChain","Gen-AI"])
st.write("Your selections:", multiselect_selection)
slider_ip=st.slider("Select a value:", min_value=0, max_value=10,value=5, step=1)
st.write("Your slider value:", slider_ip)
#select slider
select_slider_ip=st.select_slider("Select a value:", options=[1,4,20,15.5,True,'NLP',10,'ML'])
st.write("Your select slider value:", select_slider_ip)
