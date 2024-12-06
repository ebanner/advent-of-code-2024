import sys


def copy(map):
    map_copy = [row[:] for row in map]
    return map_copy


def get_map():
    map = [list(line.strip()) for line in sys.stdin.readlines()]
    return map


def get_guard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^' or map[i][j] == '>' or map[i][j] == 'V' or map[i][j] == '<':
                return i, j


def move(guard, map, visited):
    i, j = guard

    n = len(map)
    m = len(map[0])

    if map[i][j] == '^':
        while True:
            if visited[i][j] == '^':
                return 'CYCLE'
            elif i == 0:
                return 'GOAL'
            elif map[i-1][j] == '#':
                break
            visited[i][j] = '^'
            i -= 1
        map[i][j] = '>'
    elif map[i][j] == '>':
        while True:
            if visited[i][j] == '>':
                return 'CYCLE'
            elif j == m-1:
                return 'GOAL'
            elif map[i][j+1] == '#':
                break
            visited[i][j] = '>'
            j += 1
        map[i][j] = 'V'
    elif map[i][j] == 'V':
        while True:
            if visited[i][j] == 'V':
                return 'CYCLE'
            elif i == n-1:
                return 'GOAL'
            elif map[i+1][j] == '#':
                break
            visited[i][j] = 'V'
            i += 1
        map[i][j] = '<'
    elif map[i][j] == '<':
        while True:
            if visited[i][j-1] == '<':
                return 'CYCLE'
            elif j == 0:
                return 'GOAL'
            elif map[i][j-1] == '#':
                break
            visited[i][j] = '<'
            j -= 1
        map[i][j] = '^'

    return i, j


def run_simulation(guard, map):
    start_location = guard
    visited = copy(map)
    i, j = guard
    visited[i][j] = '.'
    guard = move(guard, map, visited)
    while True:
        result = move(guard, map, visited)
        if result == 'CYCLE':
            return True
        elif result == 'GOAL':
            return False

        guard = result

    return guard


def is_goal_state(guard, map):
    i, j = guard
    n = len(map)
    m = len(map[0])
    return i == 0 or i == n-1 or j == 0 or j == m-1


if __name__ == '__main__':
    map = get_map()
    start_location = get_guard(map)

    num_time_paradoxes = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '#':
                continue

            if (i, j) == start_location:
                continue

            map_copy = copy(map)
            map_copy[i][j] = '#'
            result = run_simulation(start_location, map_copy)
            if result == True:
                num_time_paradoxes += 1

    print(num_time_paradoxes)

