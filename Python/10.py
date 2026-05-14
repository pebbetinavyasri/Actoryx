def sum_of_digits(num):
    result = 0
    while num > 0:
       digit = num % 10
       result = result + digit 
       num = num // 10
    print("Sum of digits:",result)

num = int(input("Enter a number: "))
sum_of_digits(num)