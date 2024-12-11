with open("input-09.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 2333133121414131402
# """.splitlines()][1:]
# # Example answer for part 1 = 1928
# # Example answer for part 2 = 2858


def list_file_blocks(disk_map: str) -> list[int]:
    file_blocks = []
    for i in range(len(disk_map)):
        block_length = int(disk_map[i])
        if i % 2 == 0:
            file_blocks.extend([int(i/2)] * block_length)
        else:
            file_blocks.extend([None] * block_length)
    return file_blocks

def defrag_file_blocks(file_blocks: list[int]) -> list[int]:
    while None in file_blocks:
        end_val = file_blocks.pop()
        if end_val != None:
            file_blocks[file_blocks.index(None)] = end_val
    return file_blocks

def defrag_file_blocks_2(file_blocks: list[int]) -> list[int]:
    start_points = {i: 0 for i in range(1, 10)}
    for id in reversed(range(1, file_blocks[-1] + 1)):
        print('Progress', id)
        index = file_blocks.index(id)
        length = file_blocks.count(id)
        for i in range(start_points[length], index):
            if file_blocks[i:i+length] == [None] * length:
                file_blocks[i:i+length] = [id] * length
                file_blocks[index:index+length] = [None] * length
                start_points[length] = i + length
                break
    return file_blocks

def calc_checksum(file_blocks: list[int]) -> int:
    return sum([i * file_blocks[i] for i in range(len(file_blocks)) if file_blocks[i] is not None])


disk_map = lines[0]

file_blocks = list_file_blocks(disk_map)
file_blocks = defrag_file_blocks(file_blocks)
print('Part 1:', calc_checksum(file_blocks))

file_blocks = list_file_blocks(disk_map)
file_blocks = defrag_file_blocks_2(file_blocks)
print('Part 2:', calc_checksum(file_blocks))
