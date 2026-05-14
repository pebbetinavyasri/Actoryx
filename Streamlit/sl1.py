import streamlit as st

st.title("Odd or Even Checker")

# User input
num = st.number_input("Enter a number:", step=1)

# Button
if st.button("Check"):
    if num % 2 == 0:
        st.success(f"{int(num)} is an even number")
    else:
        st.warning(f"{int(num)} is an odd number")