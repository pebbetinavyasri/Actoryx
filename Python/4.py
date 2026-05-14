def check_sign(num):
    if num > 0:
        print(num,"Positive number")
    elif num < 0:
        print(num,"Negative number")
    else:
        print("Zero")

num = int(input("Enter a number: "))
check_sign(num)