import sys

def get_puzzle():
    puzzle = [line.strip() for line in sys.stdin]
    return puzzle


def eq(puzzle, i, j, value):
    n = len(puzzle)
    m = len(puzzle[0])
    return 0 <= i < len(puzzle) and 0 <= j < len(puzzle[0]) and puzzle[i][j] == value


def check_e(p, i, j):
    return eq(p, i, j, 'X') and eq(p, i, j+1, 'M') and eq(p, i, j+2, 'A') and eq(p, i, j+3, 'S')

def check_se(p, i, j):
    return eq(p, i, j,   'X') and \
            eq(p, i+1, j+1, 'M') and \
             eq(p, i+2, j+2,   'A') and \
              eq(p, i+3, j+3,     'S')

def check_s(p, i, j):
    return eq(p, i, j,   'X') and \
           eq(p, i+1, j, 'M') and \
           eq(p, i+2, j, 'A') and \
           eq(p, i+3, j, 'S')


def check_sw(p, i, j):
    return eq(p, i, j,     'X') and \
        eq(p, i+1, j-1, 'M') and \
     eq(p, i+2, j-2, 'A') and \
  eq(p, i+3, j-3, 'S')


def check_w(p, i, j):
    return eq(p, i, j-3, 'S') and eq(p, i, j-2, 'A') and eq(p, i, j-1, 'M') and eq(p, i, j, 'X')


def check_nw(p, i, j):
    return eq(p, i-3, j-3, 'S') and \
            eq(p, i-2, j-2,   'A') and \
             eq(p, i-1, j-1,      'M') and \
              eq(p, i, j,            'X')


def check_n(p, i, j):
    return eq(p, i-3, j, 'S') and \
           eq(p, i-2, j, 'A') and \
           eq(p, i-1, j, 'M') and \
           eq(p, i, j,   'X')


def check_ne(p, i, j):
    return eq(p, i-3, j+3, 'S') and \
        eq(p, i-2, j+2, 'A') and \
     eq(p, i-1, j+1, 'M') and \
  eq(p, i, j,     'X')


def get_num_xmas(puzzle: list[list[str]]):
    num_xmas = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0]):
            num_xmas += check_e(puzzle, i, j)
            num_xmas += check_se(puzzle, i, j)
            num_xmas += check_s(puzzle, i, j)
            num_xmas += check_sw(puzzle, i, j)
            num_xmas += check_w(puzzle, i, j)
            num_xmas += check_nw(puzzle, i, j)
            num_xmas += check_n(puzzle, i, j)
            num_xmas += check_ne(puzzle, i, j)
    return num_xmas


if __name__ == '__main__':
    puzzle = get_puzzle()
    num_xmas = get_num_xmas(puzzle)
    print(num_xmas)
