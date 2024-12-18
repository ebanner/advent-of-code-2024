import sys

import heapq


def get_map():
    map = [list(line.strip()) for line in sys.stdin.readlines()]
    return map


def get_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                return (i, j, 'E')


def get_end(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
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


def get_neighbors(i, j, direction, map):
    n = len(map)
    m = len(map[0])

    neighbors = []

    if direction == 'E':
        if j < m-1 and map[i][j+1] != '#':
            node = (i, j+1, direction)
            cost = 1
            neighbor = (node, cost)
            neighbors.append(neighbor)

    elif direction == 'S' and map[i+1][j] != '#':
        if i < n-1:
            node = (i+1, j, direction)
            cost = 1
            neighbor = (node, cost)
            neighbors.append(neighbor)

    elif direction == 'W' and map[i][j-1] != '#':
        if j > 0:
            node = (i, j-1, direction)
            cost = 1
            neighbor = (node, cost)
            neighbors.append(neighbor)

    elif direction == 'N' and map[i-1][j] != '#':
        if i > 0:
            node = (i-1, j, direction)
            cost = 1
            neighbor = (node, cost)
            neighbors.append(neighbor)

    node = (i, j, turn_clockwise(direction))
    cost = 1000
    neighbor = (node, cost)
    neighbors.append(neighbor)

    node = (i, j, turn_counter_clockwise(direction))
    cost = 1000
    neighbor = (node, cost)
    neighbors.append(neighbor)

    return neighbors


def cull_paths(paths):
    def get_min_cost(incoming_edges):
        min_cost = min(cost for (_, _, _, cost) in incoming_edges)
        return min_cost

    for node, incoming_edges in paths.items():
        min_cost = get_min_cost(incoming_edges)
        paths[node] = [(i, j, direction, cost) for (i, j, direction, cost) in incoming_edges if cost == min_cost]
        paths[node] = list(set(paths[node]))

    return paths


def find_shortest_paths(start, end, map):
    heap = []

    i, j, direction = start
    cost = 0
    node = (cost, i, j, direction)
    add(node, heap)

    visited = set()
    paths = {}

    paths[(i, j, direction)] = [(None, None, None, 0)]

    # print('paths', paths)
    # print()
    # print(' --- ')
    # print()

    while heap:
        # for row in map:
        #     print(''.join(row))
        # print()

        # print('HEAP', heap)
        # print()

        node = get_smallest(heap)

        (cost, i, j, direction) = node

        visited.add((i, j, direction))

        neighbors = get_neighbors(i, j, direction, map)
        for (new_i, new_j, new_direction), edge_cost in get_neighbors(i, j, direction, map):
            # print('RELAXING', f'(i={new_i}, j={new_j}, direction={new_direction}, cost={cost+edge_cost}')
            # print()

            if (new_i, new_j, new_direction) not in paths:
                paths[(new_i, new_j, new_direction)] = []
            paths[(new_i, new_j, new_direction)].append((i, j, direction, cost+edge_cost))

            if (new_i, new_j, new_direction) in visited:
                continue

            new_node = (cost+edge_cost, new_i, new_j, new_direction)
            add(new_node, heap)

    shortest_paths = cull_paths(paths)

    return paths


def reverse_direction(direction):
    return {
        None: None,
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }[direction]


def reverse(shortest_paths):
    shortest_paths_reversed = {}
    for (i, j, direction), incoming_edges in shortest_paths.items():
        reversed = []
        for (prev_i, prev_j, prev_direction, _) in incoming_edges:
            reversed.append((prev_i, prev_j, reverse_direction(prev_direction)))

        shortest_paths_reversed[(i, j, reverse_direction(direction))] = reversed

    return shortest_paths_reversed


def dfs(node, end, reversed_shortest_paths, visited):
    # print(f'dfs({node})')

    visited.add(node)

    (i, j, _) = node
    # print('i, j', i, j)
    # print('end', end)
    if (i, j) == end:
        return 1

    for neighbor in reversed_shortest_paths[node]:
        if neighbor in visited:
            continue

        dfs(neighbor, end, reversed_shortest_paths, visited)


def get_goal_states(end, shortest_paths):
    goal_states = []
    for (i, j, direction) in shortest_paths:
        if (i, j) == end:
            goal_state = (i, j, direction)
            goal_states.append(goal_state)
    return goal_states


def get_min_goal_state(end, shortest_paths):
    min_cost = float('inf')
    min_goal_state_position = None

    goal_states = get_goal_states(end, shortest_paths)
    for goal_state in goal_states:
        incoming_edges = shortest_paths[goal_state]

        for (_, _, _, cost) in incoming_edges:
            if cost < min_cost:
                min_cost = cost
                min_goal_state = goal_state

    return min_goal_state


def get_num_tiles(map):
    num_tiles = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'O':
                num_tiles += 1
    return num_tiles


if __name__ == '__main__':
    map = get_map()

    start = get_start(map)
    end = get_end(map)

    # for row in map:
    #     print(''.join(row))
    # print()

    shortest_paths = find_shortest_paths(start, end, map)
    # print('SHORTEST PATHS')
    # for key, value in sorted(shortest_paths.items()):
    #     print(key, value)
    # print()

    # for row in map:
    #     print(''.join(row))
    # print()

    reversed_shortest_paths = reverse(shortest_paths)
    # print('REVERSED SHORTEST PATHS')
    # for key, value in sorted(reversed_shortest_paths.items()):
    #     print(key, value)
    # print()

    (i, j, direction) = get_min_goal_state(end, shortest_paths)
    reversed_goal_state = (i, j, reverse_direction(direction))

    # print('STARTING GOAL STATE', reversed_goal_state)
    # print()

    visited = set()
    (i, j, _) = start
    num_tiles_shortest_paths = dfs(reversed_goal_state, (i, j), reversed_shortest_paths, visited)

    for (i, j, _) in visited:
        map[i][j] = 'O'

    # print(visited)
    # print()

    # for row in map:
    #     print(''.join(row))
    # print()

    num_tiles = get_num_tiles(map)

    print(num_tiles)

