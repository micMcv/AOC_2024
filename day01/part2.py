from input import load_input_from_aoc_website

left_numbers = []
right_numbers = []
data = load_input_from_aoc_website(day = 1).split()

for n in range(len(data)):
    if n % 2:
        right_numbers.append(int(data[n]))
    else:
        left_numbers.append(int(data[n]))

print(sum(number * right_numbers.count(number) for number in left_numbers))
