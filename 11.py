with open("input-11.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 125 17
# """.splitlines()][1:]
# # Example answer for part 1 after 25 blinks = 55312

def blink(stones: list[int]) -> list[int]:
    next_stones = []
    # naive approach
    for stone in stones:
        if stone == 0:
            next_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            next_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
            next_stones.append(int(str(stone)[int(len(str(stone))/2):]))
        else:
            next_stones.append(stone * 2024)
    return next_stones


stones = [int(x) for x in lines[0].split()]

for i in range(25):
    stones = blink(stones)

print('Part 1:', len(stones))
