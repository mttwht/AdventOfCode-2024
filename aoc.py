
def read_file_lines(filename: str) -> list[str]:
    '''Read and return all lines of text from a file'''
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def read_lines(input_text: str) -> list[str]:
    lines = input_text.splitlines()
    if lines[0] == '': lines.pop(0)
    if lines[-1] == '': lines.pop()
    return [line.strip() for line in lines]

def print_grid(grid: list[list[str]]):
    for row in grid:
        if row is str:
            print(row)
        elif type(row) is list:
            print("".join(row))
