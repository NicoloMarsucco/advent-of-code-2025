from solutions.utils import load_input

def part1(data: str) -> int:
    banks = data.splitlines()
    n = len(banks[0])
    res = 0
    for bank in banks:
        prior_max = [bank[0]]   #Max digit up and including i
        post_max = ["0"]
        for i in range(1,n):
            prior_max.append(max(prior_max[-1],bank[i]))
            post_max.append(max(post_max[-1],bank[n - i]))
        post_max.reverse()
        max_joltage = 0
        for i in range(len(prior_max)-1):
            curr = int(prior_max[i] + post_max[i])
            max_joltage = max(max_joltage,curr)
        res += max_joltage
    return res

def part2(data: str) -> int:
    banks = data.splitlines()
    n = len(banks[0])
    res = 0
    for bank in banks:
        dp = bank[:12]
        for i in range(12,n):
            curr_best = dp
            for j in range(12):
                possible_sol = dp[:j] + dp[j+1:] + bank[i]
                curr_best = max(curr_best, possible_sol)
            dp = curr_best
        res += int(dp)
    return res

if __name__ == "__main__":
    data = load_input(3)
    print(f"Part 1: {part1(data)} ")
    print(f"Part 2: {part2(data)} ")