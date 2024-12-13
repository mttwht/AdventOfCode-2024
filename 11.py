with open("input-11.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 125 17
# """.splitlines()][1:]
# # Example answer for part 1 after 25 blinks = 55312
# # Example answer for part 1 after 75 blinks = ???


def blink(stones: dict[int, int]) -> dict[int, int]:
    next_stones = dict()
    for stone, qty in stones.items():
        new_stones = []
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:int(len(str(stone))/2)]))
            new_stones.append(int(str(stone)[int(len(str(stone))/2):]))
        else:
            new_stones.append(stone * 2024)

        for new_stone in new_stones:
            if new_stone not in next_stones:
                next_stones[new_stone] = 0
            next_stones[new_stone] += qty

    return next_stones


stones = [int(x) for x in lines[0].split()]
stones = {x: stones.count(x) for x in stones}

for i in range(25):
    stones = blink(stones)
print('Part 1:', sum(stones.values()))

for i in range(50):
    print(i+1)
    stones = blink(stones)
print('Part 2:', sum(stones.values()))
