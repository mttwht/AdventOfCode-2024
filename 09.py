with open("input-09.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 2333133121414131402
# """.splitlines()][1:]
# # Example answer for part 1 = 1928


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

def calc_checksum(file_blocks: list[int]) -> int:
    return sum([i * file_blocks[i] for i in range(len(file_blocks))])


disk_map = lines[0]
file_blocks = list_file_blocks(disk_map)
file_blocks = defrag_file_blocks(file_blocks)
print(calc_checksum(file_blocks))
