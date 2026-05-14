def oddeven(num):
    if num % 2 == 0:
        print(num,"is a even number")
    else:
        print(num,"is an odd number")

num = int(input("Enter a number: "))
oddeven(num)