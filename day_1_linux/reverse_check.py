import numpy as np
#import numpy.typing as npt

def reverse_check(a) -> bool:
    a_reverse = np.flip(a)
    return (a_reverse == a).all()

a_1 = np.array([1,2,3,4,5])
a_2 = np.array([1,2,3,2,1])
print("reverse_check(a = {}): {}".format(a_1, reverse_check(a_1)))
print("reverse_check(a = {}): {}".format(a_2, reverse_check(a_2)))


