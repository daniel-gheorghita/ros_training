import numpy as np
from typing import Tuple

def max_min_2d_array(a) -> Tuple[int, int]:
    min_axis_1 = np.min(a, axis = 1)
    max_axis_0 = np.max(a, axis = 0)
    return max_axis_0, min_axis_1

a = np.array([[1,2,3,4],[5, 6, 7, 8], [9, 10, 11, 12]])

print("max_min_2d_array(a = {}): {}".format(a, max_min_2d_array(a)))
