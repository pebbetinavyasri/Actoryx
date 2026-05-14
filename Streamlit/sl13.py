import streamlit as st

st.title("Prime Number Checker")


# Function
def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False


# User input
num = st.number_input("Enter a number:", min_value=0, step=1)

# Button
if st.button("Check Prime"):

    if check_prime(int(num)):
        st.success(f"{int(num)} is a prime number")
    else:
        st.error(f"{int(num)} is not a prime number")