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


def parse(input: list[str]) -> tuple[list[str], list[str]]:
    patterns, designs = [], []
    for line in input:
        if ',' in line:
            patterns = line.split(', ')
        elif len(line) > 0:
            designs.append(line)
    return patterns, designs

# def can_make_design(patterns: list[str], design: str) -> list[list[str]]:
#     designs = []
#     for pattern in patterns:
#         if design == pattern:
#             designs.append([pattern])
#         elif design.startswith(pattern):
#             for d in can_make_design(patterns, design[len(pattern):]):
#                 designs.append([pattern] + d)
#     return designs

impossible_patterns = set()
def can_make_design(patterns: list[str], design: str) -> list[list[str]]:
    global impossible_patterns
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

patterns, designs = parse(input)
patterns.sort(key=lambda x : len(x), reverse=True)

answer = 0
for design in designs:
    solutions = can_make_design(patterns, design)
    print(design, solutions)
    if solutions:
        answer += 1

print('Part 1:', answer)
