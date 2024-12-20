import sys


def get_map():
    map = [list(line.strip()) for line in sys.stdin.readlines()]
    return map


def get_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                map[i][j] = '.'
                return (i, j)


def get_end(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'E':
                map[i][j] = '.'
                return (i, j)


def get_times(start, end, map):
    times = copy(map)

    n = len(times)
    m = len(times[0])

    picoseconds = 0

    pos = start
    i, j = pos

    while True:
        times[i][j] = picoseconds

        if pos == end:
            break

        if times[i-1][j] == '.':
            pos = (i-1, j)
        elif times[i][j+1] == '.':
            pos = (i, j+1)
        elif times[i+1][j] == '.':
            pos = (i+1, j)
        elif times[i][j-1] == '.':
            pos = (i, j-1)

        picoseconds += 1

        (i, j) = pos

    return times


def bfs(i, j, level, map):
    def get_neighbors(i, j):
        neighbors = [
                     (i-1, j),
            (i, j-1),         (i, j+1),
                     (i+1, j),
        ]
        return neighbors

    n = len(map)
    m = len(map[0])

    frontier = [(i, j)]

    visited = set()
    for _ in range(level):
        new_frontier = []
        for (i, j) in frontier:
            for (neighbor_i, neighbor_j) in get_neighbors(i, j):
                if (neighbor_i, neighbor_j) in visited:
                    continue

                if 0 <= neighbor_i < n and 0 <= neighbor_j <m:
                    visited.add((neighbor_i, neighbor_j))
                    new_frontier.append((neighbor_i, neighbor_j))

        frontier = new_frontier

    return visited


def get_cheat_times(start, end, reversed_times, original_map):
    def add(num_save, cheats):
        if num_save not in cheats:
            cheats[num_save] = 0
        cheats[num_save] += 1

    def get_distance(i, j, cheat_i, cheat_j):
        distance = abs(i-cheat_i) + abs(j-cheat_j)
        return distance

    map = copy(original_map)

    n = len(map)
    m = len(map[0])

    pos = start
    i, j = pos

    picoseconds = reversed_times[i][j]

    cheats = {}
    while True:
        if pos == end:
            break

        max_save = 0
        min_time = reversed_times[i][j]

        LEVEL = 20
        neighbors = bfs(i, j, LEVEL, map)
        for (cheat_i, cheat_j) in neighbors:
            if map[cheat_i][cheat_j] == '#':
                continue

            cheat_picoseconds = reversed_times[cheat_i][cheat_j]
            dist = get_distance(i, j, cheat_i, cheat_j)
            if dist+cheat_picoseconds < picoseconds:
                num_save = picoseconds - (dist+cheat_picoseconds)
                add(num_save, cheats)

        map[i][j] = 'O'

        if map[i-1][j] == '.':
            pos = (i-1, j)
        elif map[i][j+1] == '.':
            pos = (i, j+1)
        elif map[i+1][j] == '.':
            pos = (i+1, j)
        elif map[i][j-1] == '.':
            pos = (i, j-1)

        (i, j) = pos

        picoseconds = reversed_times[i][j]

    return cheats


def reverse_times(end, start, times, map):
    reversed_times = copy(map)

    pos = end
    (i, j) = pos

    total_picoseconds = times[i][j]

    while True:
        reversed_times[i][j] = total_picoseconds - times[i][j]

        if pos == start:
            break

        if reversed_times[i-1][j] == '.':
            pos = (i-1, j)
        elif reversed_times[i][j+1] == '.':
            pos = (i, j+1)
        elif reversed_times[i+1][j] == '.':
            pos = (i+1, j)
        elif reversed_times[i][j-1] == '.':
            pos = (i, j-1)

        (i, j) = pos

    return reversed_times


def copy(map):
    map_copy = [row[:] for row in map]
    return map_copy


if __name__ == '__main__':
    map = get_map()

    start = get_start(map)
    end = get_end(map)

    times = get_times(start, end, map)
    reversed_times = reverse_times(end, start, times, map)
    cheats = get_cheat_times(start, end, reversed_times, map)

    num_save_atleast_100 = sum(count for num_save, count in cheats.items() if num_save >= 100)

    print(num_save_atleast_100)

