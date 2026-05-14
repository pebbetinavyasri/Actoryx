import streamlit as st

st.title("Factorial Calculator")

# Function
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# User input
num = st.number_input("Enter a number:", min_value=0, step=1)

# Button
if st.button("Calculate Factorial"):
    result = factorial(int(num))
    st.success(f"Factorial of {int(num)} is {result}")