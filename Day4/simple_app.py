import streamlit as st
st.title("My first Streamlit App!!!")
st.header("Welcome to my AI Application !")
name= st.text_input("enter Your name:")
if st.button("Submit"):
    st.write("hello",name)
chat=st.chat_input("Enter Your question:")
st.checkbox("Male")
st.checkbox("Female")
st.number_input("Enter Your age")
st.slider("Pick a number",0,100)