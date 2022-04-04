from typing import List

def find_divisible(values: List[int], divisor = 5) -> List[int]:
    divisible_values = [x for x in values if x % divisor == 0]
    return divisible_values

list_of_numbers = list(range(50))
divisor = 5
print("find_divisible(values = {}, divisor = {}): {}".format(list_of_numbers, divisor, find_divisible(list_of_numbers, divisor)))
