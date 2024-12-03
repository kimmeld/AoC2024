def is_safe(report):
    """
    Helper function to determine if a given report is safe
    """
    inc = False
    dec = False
    safe_levels = True

    last = -1
    for i in report:
        if last == -1:
            last = i
        else:
            if abs(last - i) < 1 or abs(last - i) > 3:
                safe_levels = False
            if last > i:
                dec = True
            if last < i:
                inc = True
            last = i
    if safe_levels and inc != dec:
        return True
    return False

with open("day02.input") as f:
    num_safe = 0
    num_safe_pt2 = 0
    for l in f.readlines():
        report = [int(x) for x in l.split()]

        # Part 1 - how many reports are safe?
        if is_safe(report):
            num_safe += 1

        # Part 2 - how many reports can be made safe by removing one level?
        is_safe_pt2 = False
        for rm in range(len(report)):
            new_report = report.copy()
            del new_report[rm]
            if is_safe(new_report):
                is_safe_pt2 = True
        if is_safe_pt2:
            num_safe_pt2 += 1

    print(f"Part 1 = {num_safe}")
    print(f"Part 2 = {num_safe_pt2}")