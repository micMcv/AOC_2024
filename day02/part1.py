from input import load_input_from_aoc_website

result = 0
data = load_input_from_aoc_website(year = 2024 , day = 2).splitlines()

def distance_greater_three(a : int,b : int):
    return abs(a-b) > 3

def is_safe (line_ ):
    check = True

    line_ = list(map(int, line_.split(" ")))

    first = line_[0]
    second = line_[1]
    if second == first or distance_greater_three(second, first):
        return False
    if second > first:

        for n in range(2, len(line_)):
            if line_[n] <= line_[n - 1] or distance_greater_three(line_[n], line_[n - 1]):
                return False

    else:
        for n in range(2, len(line_)):
            if line_[n] >= line_[n - 1] or distance_greater_three(line_[n - 1], line_[n]):
                return False

    return check

for line in data:

    if is_safe(line):
        result += 1

print(result)