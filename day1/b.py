import sys


def get_counts(B):
    counts = {}
    for b in B:
        if b not in counts:
            counts[b] = 0
        counts[b] += 1
    return counts


def main(A: list[int], B: list[int]):
    counts = get_counts(B)
    sum = 0
    for a in A:
        sum += a*counts.get(a, 0)

    return sum


if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin]
    A, B = [], []
    for line in lines:
        a, b = line.split()
        A.append(int(a))
        B.append(int(b))

    result = main(A, B)
    print(result)
