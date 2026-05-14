import streamlit as st

st.title("Multiplication Table")

num = 9

st.write(f"### Multiplication Table of {num}")

for i in range(1, 11):
    st.write(f"{num} x {i} = {num * i}")