import aoc


input = aoc.read_file_lines("input-19.txt")

# input = aoc.read_lines("""
# r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb
# """)
# # Example answer for part 1 = 6
# # Example answer for part 2 = 16


def parse(input: list[str]) -> tuple[list[str], list[str]]:
    patterns, designs = [], []
    for line in input:
        if ',' in line:
            patterns = line.split(', ')
        elif len(line) > 0:
            designs.append(line)
    return patterns, designs

impossible_patterns = set()
def can_make_design(patterns: list[str], design: str) -> list[list[str]]:
    global impossible_patterns, possibilities
    if design in impossible_patterns:
        return None
    for pattern in [p for p in patterns if design.startswith(p)]:
        if design == pattern:
            return [pattern]
        elif design.startswith(pattern):
            d = can_make_design(patterns, design[len(pattern):])
            if d:
                return [pattern] + d
    impossible_patterns.add(design)

possibilities = {}
def how_many_possibilities(patterns: list[str], design: str) -> int:
    global possibilities
    if design in impossible_patterns:
        return 0
    if design in possibilities:
        return possibilities[design]
    count = 0
    for pattern in [p for p in patterns if design.startswith(p)]:
        if design == pattern:
            count += 1
        elif design.startswith(pattern):
            count += how_many_possibilities(patterns, design[len(pattern):])
    possibilities[design] = count
    return count


patterns, designs = parse(input)

answer = len([design for design in designs if can_make_design(patterns, design)])
print('Part 1:', answer)

answer = sum([how_many_possibilities(patterns, design) for design in designs])
print('Part 2:', answer)
