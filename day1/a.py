import sys


def main(A: list[int], B: list[int]):
    difference = 0
    for a, b in zip(sorted(A), sorted(B)):
        difference += abs(a - b)
    return difference


if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin]
    A, B = [], []
    for line in lines:
        a, b = line.split()
        A.append(int(a))
        B.append(int(b))

    result = main(A, B)
    print(result)
