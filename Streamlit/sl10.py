import streamlit as st

st.title("Sum of Digits Calculator")

# User input
num = st.number_input("Enter a number:", min_value=0, step=1)

# Button
if st.button("Calculate Sum"):

    temp = int(num)
    result = 0

    while temp > 0:
        digit = temp % 10
        result = result + digit
        temp = temp // 10

    st.success(f"Sum of digits: {result}")