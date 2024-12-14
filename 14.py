import re

with open("input-14.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

P, V = 0, 1
X, Y = 0, 1
W, H = 101, 103

# lines = [line.strip() for line in """
# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3
# """.splitlines()][1:]
# W, H = 11, 7
# # Example answer for part 1 at w=11 h=7 = 12


def parse(lines: list[str]) -> list[list[tuple[int, int]]]:
    robots = []
    for line in lines:
        px, py, vx, vy = re.match(r'^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line).groups()
        robots.append([(int(px), int(py)), (int(vx), int(vy))])
    return robots

def move(robot: list[tuple[int,int]]) -> list[tuple[int,int]]:
    robot[P] = (robot[P][X] + robot[V][X], robot[P][Y] + robot[V][Y])
    return robot

def teleport(robot: list[tuple[int,int]]) -> list[tuple[int,int]]:
    robot[P] = (robot[P][X] % W, robot[P][Y] % H)
    return robot

def prod(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return 0
    prod = numbers[0]
    for n in numbers[1:]:
        prod *= n
    return prod


robots = parse(lines)

for i in range(100):
    for robot in robots:
        move(robot)
        teleport(robot)

quadrants = [[] for _ in range(4)]

for robot in robots:
    if robot[P][X] < int(W/2):
        if robot[P][Y] < int(H/2):
            quadrants[0].append(robot)
        elif robot[P][Y] > int(H/2):
            quadrants[1].append(robot)
    elif robot[P][X] > int(W/2):
        if robot[P][Y] < int(H/2):
            quadrants[2].append(robot)
        elif robot[P][Y] > int(H/2):
            quadrants[3].append(robot)

print('Part 1:', prod([len(q) for q in quadrants]))

robots = parse(lines)
f = open('14-out.txt', 'w')
for i in range(1, 10000):
    for robot in robots:
        move(robot)
        teleport(robot)
    total_x = sum([r[P][X] for r in robots])
    total_y = sum([r[P][Y] for r in robots])
    avg_x = total_x / len(robots)
    avg_y = total_y / len(robots)
    total_dist_x = sum([abs(r[P][X] - avg_x) for r in robots])
    total_dist_y = sum([abs(r[P][Y] - avg_y) for r in robots])
    avg_dist_x = total_dist_x / len(robots)
    avg_dist_y = total_dist_y / len(robots)
    if avg_dist_x < (W/5) and avg_dist_y < (H/5):
        print(i, avg_dist_x, avg_dist_y)
        
        f.write(str(i) + "\n")
        out_lines = []
        for y in range(H):
            row = ''
            for x in range(W):
                if (x, y) in [r[P] for r in robots]:
                    row += 'X'
                else:
                    row += '.'
            out_lines.append(row + "\n")
        f.writelines(out_lines)
        f.write("\n")
f.close()
