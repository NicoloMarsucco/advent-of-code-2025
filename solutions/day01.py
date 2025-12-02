from solutions.utils import load_input

def part1(data: str) -> int:
    commands = data.splitlines()
    res = 0
    dial_angle = 50
    for command in commands:
        if command[0] == 'L':
            dial_angle -= int(command[1:])
        else:
            dial_angle += int(command[1:])

        if dial_angle % 100 == 0:
            res += 1
    return res

def part2(data: str) -> int:
    commands = data.splitlines()
    res = 0
    dial_angle = 50
    for command in commands:
        if command[0] == 'L':
            delta = -int(command[1:])
        else:
            delta = int(command[1:])
        
        next_angle = dial_angle + delta
        res += abs(dial_angle // 100 - next_angle // 100)
        if dial_angle % 100 == 0 and delta < 0:
            res -= 1
        if next_angle % 100 == 0 and delta < 0:
            res += 1

        dial_angle = next_angle
    return res

if __name__ == "__main__":
    data = load_input(1)
    print(f"Part 1: {part1(data)} ")
    print(f"Part 2: {part2(data)} ")