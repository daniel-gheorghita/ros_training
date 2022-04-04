from datetime import datetime

def str_to_datetime(date_str: str):
    datetime_obj = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
    return datetime_obj

date_str = "Apr 04 2022 2:57PM"
print("str_to_datetime(date_str = {}): {}".format(date_str, str_to_datetime(date_str)))
