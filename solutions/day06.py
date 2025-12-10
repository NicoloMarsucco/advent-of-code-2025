from solutions.utils import load_input

def part1(data: str) -> int:
    separated = [line.split() for line in data.splitlines()]
    rows = len(separated)
    columns = len(separated[0])
    res = 0
    for j in range(columns):
        curr = int(separated[0][j])
        is_addition = separated[rows-1][j] == "+"
        for i in range(1,rows-1):
            if is_addition:
                curr += int(separated[i][j])
            else:
                curr *= int(separated[i][j])
        res += curr

    return res

def part2(data: str) -> int:
    data = data.split("\n")
    operators = data[-1]
    start_indexes = [i for i, ltr in enumerate(operators) if ltr == "*" or ltr == "+"]
    start_indexes.append(len(data[0])+1)

    is_addition = [operator == "+" for operator in operators.split()]

    numbers = [[row[start_indexes[i]:start_indexes[i+1]-1] for i in range(len(start_indexes)-1)] for row in data[:-1]]

    columns = len(is_addition)
    rows = len(numbers)
    res = 0

    for j in range(columns):
        curr = -1
        for k in range(len(numbers[0][j])):
            curr_num = ""
            for i in range(rows):
                char = numbers[i][j][k]
                if char != " ":
                    curr_num += char
            
            if curr == -1:
                curr = int(curr_num)
            elif is_addition[j]:
                curr += int(curr_num)
            else:
                curr *= int(curr_num)
        
        res += curr

    return res
         
if __name__ == "__main__":
    data = load_input(6)
    print(f"Part 1: {part1(data)} ")
    print(f"Part 2: {part2(data)} ")