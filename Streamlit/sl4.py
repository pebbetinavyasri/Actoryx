import streamlit as st

st.title("Positive, Negative or Zero Checker")

# User input
num = st.number_input("Enter a number:", step=1)

# Button
if st.button("Check Sign"):
    if num > 0:
        st.success(f"{int(num)} is a Positive number")
    elif num < 0:
        st.warning(f"{int(num)} is a Negative number")
    else:
        st.info("The number is Zero")