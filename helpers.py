import re
import collections

def get_ints(string  , mode="int_list"):
    if mode == "int_list":
        return re.findall(r"[0-9]+" , string)


