import streamlit as st

st.title("Voting Eligibility Checker")

# User input
age = st.number_input("Enter your age:", min_value=0, step=1)

# Button
if st.button("Check Eligibility"):
    if age >= 18:
        st.success("Eligible to vote")
    else:
        st.error("Not Eligible to vote")