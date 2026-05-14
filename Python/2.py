def checkvote(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")

age = int(input("Enter age: "))
checkvote(age)
    