from input import load_input_from_aoc_website
import re

def mul(a,b):
    return a*b

def get_multiplications(string):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern , string)

def sum_of_multiplications(matches):
    result = 0
    for match in matches:
        result += eval(match)
    return result

data = load_input_from_aoc_website(year = 2024 , day = 3)

print(sum_of_multiplications(get_multiplications(data)))