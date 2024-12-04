import sys

def get_puzzle():
    puzzle = [line.strip() for line in sys.stdin]
    return puzzle


def eq(puzzle, i, j, value):
    n = len(puzzle)
    m = len(puzzle[0])
    return 0 <= i < len(puzzle) and 0 <= j < len(puzzle[0]) and puzzle[i][j] == value


def check_forward_forward(p, i, j):
    return eq(p, i-1, j-1, 'M') and eq(p, i-1, j+1, 'S') and \
                    eq(p, i, j, 'A') and \
           eq(p, i+1, j-1, 'M') and eq(p, i+1, j+1, 'S')

def check_forward_backward(p, i, j):
    return eq(p, i-1, j-1, 'M') and eq(p, i-1, j+1, 'M') and \
                    eq(p, i, j, 'A') and \
           eq(p, i+1, j-1, 'S') and eq(p, i+1, j+1, 'S')


def check_backward_forward(p, i, j):
    return eq(p, i-1, j-1, 'S') and eq(p, i-1, j+1, 'S') and \
                    eq(p, i, j, 'A') and \
           eq(p, i+1, j-1, 'M') and eq(p, i+1, j+1, 'M')


def check_backward_backward(p, i, j):
    return eq(p, i-1, j-1, 'S') and eq(p, i-1, j+1, 'M') and \
                    eq(p, i, j, 'A') and \
           eq(p, i+1, j-1, 'S') and eq(p, i+1, j+1, 'M')


def get_num_xmas(puzzle: list[list[str]]):
    num_xmas = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            num_xmas += check_forward_forward(puzzle, i, j)
            num_xmas += check_forward_backward(puzzle, i, j)
            num_xmas += check_backward_forward(puzzle, i, j)
            num_xmas += check_backward_backward(puzzle, i, j)
    return num_xmas


if __name__ == '__main__':
    puzzle = get_puzzle()
    num_xmas = get_num_xmas(puzzle)
    print(num_xmas)
