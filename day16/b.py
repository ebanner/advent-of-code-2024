import sys

import heapq


def get_map():
    map = [list(line.strip()) for line in sys.stdin.readlines()]
    return map


def get_start(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 'S':
                return (i, j, 'E')


def get_end(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 'E':
                return (i, j)


def add(node, heap):
    heapq.heappush(heap, node)


def get_smallest(heap):
    smallest = heapq.heappop(heap)
    return smallest


def turn_clockwise(direction):
    new_direction = {
        'E': 'S',
        'S': 'W',
        'W': 'N',
        'N': 'E'
    }[direction]

    return new_direction


def turn_counter_clockwise(direction):
    new_direction = {
        'E': 'N',
        'N': 'W',
        'W': 'S',
        'S': 'E'
    }[direction]

    return new_direction


def get_neighbors(i, j, direction, path_length, map):
    n = len(map)
    m = len(map[0])

    neighbors = []

    if direction == 'E':
        if j < m-1 and map[i][j+1] != '#':
            node = (i, j+1, direction)
            cost = 1
            neighbor = (node, cost, path_length+1)
            neighbors.append(neighbor)

    elif direction == 'S' and map[i+1][j] != '#':
        if i < n-1:
            node = (i+1, j, direction)
            cost = 1
            neighbor = (node, cost, path_length+1)
            neighbors.append(neighbor)

    elif direction == 'W' and map[i][j-1] != '#':
        if j > 0:
            node = (i, j-1, direction)
            cost = 1
            neighbor = (node, cost, path_length+1)
            neighbors.append(neighbor)

    elif direction == 'N' and map[i-1][j] != '#':
        if i > 0:
            node = (i-1, j, direction)
            cost = 1
            neighbor = (node, cost, path_length+1)
            neighbors.append(neighbor)

    node = (i, j, turn_clockwise(direction))
    cost = 1000
    neighbor = (node, cost, path_length)
    neighbors.append(neighbor)

    node = (i, j, turn_counter_clockwise(direction))
    cost = 1000
    neighbor = (node, cost, path_length)
    neighbors.append(neighbor)

    return neighbors


def find_shortest_path_cost(start, end, map):
    heap = []

    i, j, direction = start
    cost = 0
    path_length = 1
    node = (cost, i, j, direction, path_length)
    add(node, heap)

    visited = set()

    while True:
        node = get_smallest(heap)

        (cost, i, j, direction, path_length) = node
        if (i, j) == end:
            print('path length', path_length)
            return cost

        visited.add((i, j, direction))

        for (new_i, new_j, new_direction), edge_cost, new_path_length in get_neighbors(i, j, direction, path_length, map):
            if (new_i, new_j, new_direction) in visited:
                continue

            new_node = (cost+edge_cost, new_i, new_j, new_direction, new_path_length)
            add(new_node, heap)


if __name__ == '__main__':
    map = get_map()

    start = get_start(map)
    end = get_end(map)

    shortest_path_cost = find_shortest_path_cost(start, end, map)

    print(shortest_path_cost)
