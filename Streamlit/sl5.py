import streamlit as st

st.title("Arithmetic Operations Calculator")

# User inputs
num1 = st.number_input("Enter first number:", step=1.0)
num2 = st.number_input("Enter second number:", step=1.0)

# Button
if st.button("Calculate"):
    st.write("### Results")
    st.write("Addition:", num1 + num2)
    st.write("Subtraction:", num1 - num2)
    st.write("Multiplication:", num1 * num2)

    if num2 != 0:
        st.write("Division:", num1 / num2)
        st.write("Modulus:", num1 % num2)
    else:
        st.error("Division and Modulus by zero are not allowed")