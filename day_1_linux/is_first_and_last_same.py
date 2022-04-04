from typing import List
def is_first_and_last_same(values: List[int]) -> bool:
    return values[0] == values[-1]

list_of_numbers = [1, 2, 3, 4, 5, 6]
another_list_of_numbers = [1, 2, 3, 3, 2, 1]

print("is_first_and_last_same({}): {}".format(list_of_numbers, is_first_and_last_same(list_of_numbers)))
print("is_first_and_last_same({}): {}".format(another_list_of_numbers, is_first_and_last_same(another_list_of_numbers)))
