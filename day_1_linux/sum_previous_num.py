def sum_previous_num(n = 10):
    previous = 0
    for i in range(n):
        print("Sum of previous 2 numbers: ", i + previous)
        previous = i

sum_previous_num(10)