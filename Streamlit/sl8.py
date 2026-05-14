import streamlit as st

st.title("Multiplication Table")

# User input
num = st.number_input("Enter a number:", step=1)

# Button
if st.button("Generate Table"):
    st.write(f"### Multiplication Table of {int(num)}")

    for i in range(1, 11):
        st.write(f"{int(num)} x {i} = {int(num) * i}")