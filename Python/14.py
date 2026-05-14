def sum_of_list(num):
    total = sum(num)
    print("Sum of elements:", total)

num = list(map(int, input("Enter list elements separated by space: ").split()))

sum_of_list(num)