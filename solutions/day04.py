from solutions.utils import load_input

def part1(data: str) -> int:
    grid, rows, columns = prepare_data(data)
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if grid[i][j] == "@" and count_neighbors(grid, i, j) < 4:
                count +=1

    return count

def prepare_data(data: str) -> tuple[list[str], int, int]:
    lines = data.splitlines()
    columns = len(lines[0])
    rows = len(lines)
    padded_data = [list(".") + list(line) + list(".") for line in lines]
    grid = [["."] * (columns + 2), *padded_data, ["."] * (columns + 2)]
    return grid, rows, columns

def count_neighbors(grid: list[str], i: int, j: int) -> int:
    top = grid[i-1][j-1:j+2]
    sides = grid[i][j-1] + grid[i][j+1]
    bottom = grid[i+1][j-1:j+2]
    return top.count("@") + sides.count("@") + bottom.count("@")

def part2(data: str) -> int:
    grid, rows, columns = prepare_data(data)
    total_count = 0
    while True:
        places_to_change = []
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if grid[i][j] == "@" and count_neighbors(grid, i, j) < 4:
                    places_to_change.append((i, j))
        
        if not places_to_change:
            return total_count
        
        total_count += len(places_to_change)
        for i, j in places_to_change:
            grid[i][j] = "."
         
if __name__ == "__main__":
    data = load_input(4)
    print(f"Part 1: {part1(data)} ")
    print(f"Part 2: {part2(data)} ")