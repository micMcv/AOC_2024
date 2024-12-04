from input import load_input_from_aoc_website

result = 0
data = load_input_from_aoc_website(year = 2024 , day = 4).splitlines()

for row in range(len(data)):
    print(data[row])
    for col in range(len(data[0])):
        if (col+3) < len(data[0]) and data[row][col] == "X" and data[row][col + 1] == "M" and data[row][col + 2] == "A" and data[row][col + 3] == "S": result += 1

        if (col+3) < len(data[0]) and data[row][col] == "S" and data[row][col + 1] == "A" and data[row][col + 2] == "M" and data[row][col + 3] == "X": result += 1

        if (row+3) < len(data) and data[row][col] == "X" and data[row + 1][col] == "M" and data[row + 2][col] == "A" and data[row + 3][col] == "S": result += 1

        if (row + 3) < len(data) and data[row][col] == "S" and data[row + 1][col] == "A" and data[row + 2][
            col] == "M" and data[row + 3][col] == "X": result += 1

        if (col + 3) < len(data[0]) and (row + 3) < len(data) and data[row][col] == "S" and data[row + 1][col +1 ] == "A" and data[row + 2][
            col + 2] == "M" and data[row + 3][col + 3] == "X": result += 1

        if (col + 3) < len(data[0]) and (row + 3) < len(data) and data[row][col] == "X" and data[row + 1][col +1 ] == "M" and data[row + 2][
            col + 2] == "A" and data[row + 3][col + 3] == "S": result += 1

        if col + 3 < len(data[0]) and row > 2 and data[row][col] == "S" and data[row - 1][col + 1 ] == "A" and data[row - 2][
            col + 2] == "M" and data[row - 3][col + 3] == "X": result += 1

        if col + 3 < len(data[0]) and row > 2  and data[row][col] == "X" and data[row - 1][col + 1 ] == "M" and data[row - 2][
            col + 2] == "A" and data[row - 3][col + 3] == "S": result += 1

print(result)