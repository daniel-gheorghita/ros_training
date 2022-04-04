from typing import List

def extract_digits(number: int) -> List[int]:
    digits = list(map(int,list(map(float,list(str(number))))))
    digits.reverse()
    return digits

number = 123456
print("extract_digits(number = {}): {}".format(number, extract_digits(number)))
