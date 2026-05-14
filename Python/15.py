def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("Average Marks:", average)
    print("Grade:", grade)

marks = list(map(int, input("Enter marks separated by space: ").split()))
calculate_grade(marks)