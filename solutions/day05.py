from solutions.utils import load_input
from intervaltree import IntervalTree

def part1(data: str) -> int:
    data = data.splitlines()
    tree = IntervalTree()

    curr_row_index = 0
    while data[curr_row_index]:
        parts = data[curr_row_index].split("-")
        tree.addi(int(parts[0]), int(parts[1]) + 1)
        curr_row_index += 1

    fresh_count = 0
    for i in range(curr_row_index+1,len(data)):
        if bool(tree[int(data[i])]):
            fresh_count += 1

    return fresh_count

def part2(data: str) -> int:
    data = data.splitlines()
    tree = IntervalTree()

    curr_row_index = 0
    while data[curr_row_index]:
        parts = data[curr_row_index].split("-")
        tree.addi(int(parts[0]), int(parts[1]) + 1)
        curr_row_index += 1
    
    tree.merge_overlaps()
    return sum(interval.end - interval.begin for interval in tree)
         
if __name__ == "__main__":
    data = load_input(5)
    print(f"Part 1: {part1(data)} ")
    print(f"Part 2: {part2(data)} ")