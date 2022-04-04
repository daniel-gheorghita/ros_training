def print_even_index_char(str):
    for i in range(0,len(str), 2):
        print("Character {} is {}".format(i, str[i]))

print_even_index_char(str = "ROS Training at IWT 2022")