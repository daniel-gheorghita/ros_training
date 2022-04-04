def remove_n_chars(str: str, n: int) -> str:
    new_string = str[n:]
    return new_string

n = 10
str = "ROS Training IWT 2022"
print("Removed first {} characters from {}: {}".format(n, str, remove_n_chars(str, n))) 
