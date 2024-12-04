from input import load_input_from_aoc_website
import re

def mul(a,b):
    return a*b

def find_mul(string):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern , string)

def sum_of_multiplications(matches):
    result = 0
    for match in matches:
        result += eval(match)
    return result

final_result = 0
data = load_input_from_aoc_website(year = 2024 , day = 3)

initial = data[0 : data.index("don't")]
final_result += sum_of_multiplications(find_mul(initial))
data = data.split("do()")[1:]

for line in data:

    do = line.split("don't")[0]
    final_result += sum_of_multiplications(find_mul(do))

print(final_result)