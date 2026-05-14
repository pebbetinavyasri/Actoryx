import streamlit as st

st.title("Student Grade Calculator")

# User input
marks_input = st.text_input("Enter marks separated by space:")

# Button
if st.button("Calculate Grade"):

    marks = list(map(int, marks_input.split()))

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    st.write(f"Average Marks: {average:.2f}")
    st.success(f"Grade: {grade}")