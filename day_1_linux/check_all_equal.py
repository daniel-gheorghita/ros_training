def check_all_equal(a: tuple) -> bool:
    return all([x == a[0] for x in a])

a = (1, 2, 3, 4, 5, 6)
b = (9, 9, 9, 9, 9, 9)
print("check_all_equal(a = {}): {}".format(a, check_all_equal(a)))
print("check_all_equal(a = {}): {}".format(b, check_all_equal(b)))

