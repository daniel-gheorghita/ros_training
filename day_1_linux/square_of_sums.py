import numpy as np

def square_of_sums(a, b):
    assert np.shape(a) == np.shape(b), "The arrays do not have the same shapes ({} != {}).".format(np.shape(a), np.shape(b))
    return (a + b) ** 2

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 11, 12, 13, 14])
b_1 = np.array([1, 2, 3])
a_2 = np.array([[1,2,3],[4,5,6]])
b_2 = np.array([[10, 11, 12],[13, 14, 15]])

print("square_of_sums(a = {}, b = {}): {}".format(a, b, square_of_sums(a, b)))
#print("square_of_sums(a = {}, b = {}): {}".format(a, b_1, square_of_sums(a, b_1)))
print("square_of_sums(a = {}, b = {}): {}".format(a_2, b_2, square_of_sums(a_2, b_2)))
print("square_of_sums(a = {}, b = {}): {}".format(a_2, b_1, square_of_sums(a_2, b_1)))
