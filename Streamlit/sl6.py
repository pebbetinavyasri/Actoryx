import streamlit as st

st.title("First 10 Natural Numbers")

st.write("First 10 Natural Numbers:")

for i in range(1, 11):
    st.write(i)