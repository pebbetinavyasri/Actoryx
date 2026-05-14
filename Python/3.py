def greatest_of_two(num1,num2):
    if num1 > num2:
        print(num1, "is greatest")
    elif num2 > num1:
        print(num2, "is greatest")
    else:
        print("Both are equal")
        
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
greatest_of_two(num1,num2)