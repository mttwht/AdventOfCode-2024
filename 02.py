with open("input-02.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """.splitlines()][1:]
# # Example answer  = 2

def parse(lines):
    return [[int(level) for level in report.split()] for report in lines]

def is_safe(report):
    for i in range(len(report)-1):
        l1, l2 = report[i:i+2]
        if l1 == l2:
            return False
        elif abs(l1 - l2) > 3:
            return False
        
        if i == 0:
            is_inc = l1 < l2
        else:
            if (l1 < l2) != is_inc:
                return False
    return True


reports = parse(lines)
safe_reports = []
for report in reports:
    if is_safe(report):
        safe_reports.append(report)

print(len(safe_reports))
