import streamlit as st

st.title("Factors Finder")


# Function
def factors(num):
    factor_list = []

    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)

    return factor_list


# User input
num = st.number_input("Enter a number:", min_value=1, step=1)

# Button
if st.button("Find Factors"):
    result = factors(int(num))

    st.write(f"### Factors of {int(num)} are:")

    for factor in result:
        st.write(factor)