import streamlit as st

st.title("First N Natural Numbers")

# User input
num = st.number_input("Enter a number:", min_value=1, step=1)

# Button
if st.button("Show Numbers"):
    st.write("### First N Natural Numbers:")

    for i in range(1, int(num) + 1):
        st.write(i)