with open("input-05.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.splitlines()][1:]
# # Example answer  = 143

def parse_input(lines: list[str]) -> tuple[list[list[str]], list[list[str]]]:
    i_sep = lines.index('')
    rules, updates = lines[:i_sep], lines[i_sep+1:]
    rules = [rule.split('|') for rule in rules]
    updates = [update.split(',') for update in updates]
    return (rules, updates)

def sum_center_pages(updates: list[list[str]]) -> int:
    return sum([int(u[int(len(u)/2)]) for u in updates])

rules, updates = parse_input(lines)
correctly_ordered_updates = []
for update in updates:
    follows_rules = True
    for rule in rules:
        if set(rule).issubset(update):
            i, j = update.index(rule[0]), update.index(rule[1])
            if i > j:
                follows_rules = False
                break
    if follows_rules:
        correctly_ordered_updates.append(update)

answer = sum_center_pages(correctly_ordered_updates)
print(answer)
