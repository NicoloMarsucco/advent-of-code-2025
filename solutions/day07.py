from solutions.utils import load_input

def part1(data: str) -> int:
    data = data.splitlines()
    curr_beams = set()
    curr_beams.add(data[0].find("S"))
    res = 0
    for i in range(2,len(data),2):
        new_beams = set()
        for beam in curr_beams:
            if data[i][beam] == "^":
                res += 1
                new_beams.add(beam-1)
                new_beams.add(beam+1)
            else:
                new_beams.add(beam)

        curr_beams = new_beams

    return res

def part2(data: str) -> int:
    data = data.splitlines()
    curr_beams = {}
    curr_beams[data[0].find("S")] = 1
    for i in range(2,len(data),2):
        new_beams = {}
        for beam, trajectories in curr_beams.items():
            if data[i][beam] == "^":
                new_beams[beam - 1] = new_beams.get(beam - 1, 0) + trajectories
                new_beams[beam + 1] = new_beams.get(beam + 1, 0) + trajectories
            else:
                new_beams[beam] = new_beams.get(beam, 0) + trajectories
        curr_beams = new_beams

    return sum(curr_beams.values())
         
if __name__ == "__main__":
    data = load_input(7)
    print(f"Part 1: {part1(data)} ")
    print(f"Part 2: {part2(data)} ")