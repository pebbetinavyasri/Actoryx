def multiplication_table(num):
    print("Multiplication Table of", num)

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

num = int(input("Enter a number: "))
multiplication_table(num)