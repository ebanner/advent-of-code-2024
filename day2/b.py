import sys

def get_reports():
    lines = [line.strip() for line in sys.stdin]
    reports = [list(map(int, line.split())) for line in lines]
    return reports


def is_safe_increasing(report: list[int]):
    for i in range(len(report) - 1):
        if report[i] < report[i + 1] and report[i + 1] - report[i] <= 3:
            continue
        else:
            return False
    return True


def is_safe_decreasing(report: list[int]):
    for i in range(len(report) - 1):
        if report[i] > report[i + 1] and report[i] - report[i + 1] <= 3:
            continue
        else:
            return False
    return True


def remove(index, arr):
  return arr[:index] + arr[index+1:]


def is_safe(report: list[int]):
    if is_safe_increasing(report):
        return True
    else:
        for i in range(len(report)):
            if is_safe_increasing(remove(i, report)):
                return True

    if is_safe_decreasing(report):
        return True
    else:
        for i in range(len(report)):
            if is_safe_decreasing(remove(i, report)):
                return True

    return False
    


def count_num_safe(reports: list[list[int]]):
    num_safe = 0
    for report in reports:
        if is_safe(report):
            num_safe += 1
    return num_safe


if __name__ == '__main__':
    reports = get_reports()
    num_safe = count_num_safe(reports)
    print(num_safe)

