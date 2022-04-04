def find_substr_count(long_str: str, short_str: str) -> int:
    return long_str.count(short_str)

long_str = "Emma is attending the ROS Training. Emma likes to learn new stuff. Be like Emma!"
short_str = "Emma"
print("find_substr_count(long_str = {}, short_str = {}): {}".format(long_str, short_str, find_substr_count(long_str, short_str)))
