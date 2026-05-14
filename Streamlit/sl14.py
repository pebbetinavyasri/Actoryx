import streamlit as st

st.title("Sum of List Elements")

# User input
numbers = st.text_input("Enter list elements separated by space:")

# Button
if st.button("Calculate Sum"):
    num_list = list(map(int, numbers.split()))

    total = sum(num_list)

    st.success(f"Sum of elements: {total}")