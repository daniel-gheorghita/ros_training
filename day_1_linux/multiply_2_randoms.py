import random
import numpy as np

#random.seed(5)
#np.random.seed(5)

def multiply_2_randoms():
    return random.randint(0, 100) * random.uniform(0, 100)

def multiply_2_randoms_numpy():
    return np.random.randint(0, 100) * np.random.uniform(0, 100)

print("multiply_2_randoms(): {}".format(multiply_2_randoms()))
print("multiply_2_randoms_numpy(): {}".format(multiply_2_randoms_numpy()))
