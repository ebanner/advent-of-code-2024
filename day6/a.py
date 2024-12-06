import sys

def get_map():
    map = [list(line.strip()) for line in sys.stdin.readlines()]
    return map


def get_guard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^' or map[i][j] == '>' or map[i][j] == 'V' or map[i][j] == '<':
                return i, j


def move(guard, map):
    i, j = guard

    n = len(map)
    m = len(map[0])

    if map[i][j] == '^':
        # print('^')
        while i > 0 and map[i-1][j] != '#':
            map[i][j] = 'X'
            i -= 1
        map[i][j] = '>'
    elif map[i][j] == '>':
        # print('>')
        while j < m-1 and map[i][j+1] != '#':
            map[i][j] = 'X'
            j += 1
        map[i][j] = 'V'
    elif map[i][j] == 'V':
        # print('V')
        while i < n-1 and map[i+1][j] != '#':
            map[i][j] = 'X'
            i += 1
        map[i][j] = '<'
    elif map[i][j] == '<':
        # print('<')
        while j > 0 and map[i][j-1] != '#':
            map[i][j] = 'X'
            j -= 1
        map[i][j] = '^'

    return i, j


def is_goal_state(guard, map):
    i, j = guard
    n = len(map)
    m = len(map[0])
    return i == 0 or i == n-1 or j == 0 or j == m-1


def count_distinct_positions(map):
    distinct_positions = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'X':
                distinct_positions += 1
    return distinct_positions


if __name__ == '__main__':
    map = get_map()
    guard = get_guard(map)

    while not is_goal_state(guard, map):
        guard = move(guard, map)

    i, j = guard
    if map[i][j] == '^':
        map[i][j] = 'X'
        i -= 1
    elif map[i][j] == '>':
        map[i][j] = 'X'
        j += 1
    elif map[i][j] == 'V':
        map[i][j] = 'X'
        i += 1
    elif map[i][j] == '<':
        map[i][j] = 'X'
        j -= 1

    distinct_positions = count_distinct_positions(map)

    print(distinct_positions)
