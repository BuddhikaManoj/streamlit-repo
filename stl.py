import streamlit as st

st.title('Welcome to My Streamlit Project')
st.write('This is a simple Streamlit app.')

# number = st.slider('Pick a number', 0, 100)
# st.write(f'You selected: {number}')

name = st.text_input('Enter your name')
feedback = st.text_area('Enter your feedback')
age = st.number_input('Enter your age')
date = st.date_input('select a date')
time = st.time_input('pick a time')
color = st.color_picker('select a color')

st.write(f'Your name is: {name} ')