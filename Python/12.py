def factors(num):
    print("Factors of", num, "are:")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

num = int(input("Enter a number: "))
factors(num)