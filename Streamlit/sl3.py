import streamlit as st

st.title("Greatest of Two Numbers")

# User inputs
num1 = st.number_input("Enter number 1:", step=1)
num2 = st.number_input("Enter number 2:", step=1)

# Button
if st.button("Find Greatest"):
    if num1 > num2:
        st.success(f"{int(num1)} is greatest")
    elif num2 > num1:
        st.success(f"{int(num2)} is greatest")
    else:
        st.info("Both numbers are equal")