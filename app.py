import streamlit as st
import numpy as np
import pandas as pd

# Adding a title of your app
st.title('My First Testing App for Codanics course(6 months long) ')

# Adding simple text
st.write('Here is a simple text')

# user input
number =st.slider('Pick a number',0,100,20 ) # 20 is a default

# print the text number
st.write(f'You selected:{number}')

# Add button
if st.button('Greeting'):
    st.write('Hi hello there')
else:
    st.write('Goodbye')

# Add ratio button with option
genra=st.radio(
    "What your favourite drama",
    ('Drilis Ertugrul','Kurlus Osman','Saluddin Auybi'))

# Add print text genra
st.write(f'What your drama {genra}')

# # Add drop down list
# option=st.selectbox(
#     "How would you like to be contacted",
#     ('Email','Home Phone','Mobile Phone'))

# Add drop down list sidebar
option=st.sidebar.selectbox(
    "How would you like to be contacted",
    ('Email','Home Phone','Mobile Phone'))

# Add your whatshap number sidebar
st.sidebar.text_input('What your whatshap number')

# Add a file uploader
file_uploader=st.sidebar.file_uploader("Choose your CSV file",type='CSV')

# Create a line Plot Plotting
data= pd.DataFrame({
    'First coloumn':list(range(1,11)),
    'Second coloumn':np.arange(number,number + 10)
})
st.line_chart(data)