import numpy as np
import random

print("Hello World!")

def mul_or_sum():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    product = number_1 * number_2 
    sum = number_1 + number_2
    if product > 1000:
        return product
    else:
        return sum

if __name__ == "__main__":
    print("Called as main.")    
    print("mul_or_sum(): ", mul_or_sum())