import sys

import itertools


def get_codes():
    codes = [line.strip() for line in sys.stdin.readlines()]
    return codes


NUMERIC_PAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}


def get_shortest_numeric_paths(source, dest):
    def get_neighbors(node):
        (i, j, _) = node

        neighbors = []
        if i-1 >= 0:
            neighbor = (i-1, j, '^')
            neighbors.append(neighbor)

        if i+1 <= 3 and (i+1, j) != (3, 0):
            neighbor = (i+1, j, 'v')
            neighbors.append(neighbor)

        if j-1 >= 0 and (i, j-1) != (3, 0):
            neighbor = (i, j-1, '<')
            neighbors.append(neighbor)

        if j+1 <= 2:
            neighbor = (i, j+1, '>')
            neighbors.append(neighbor)

        return neighbors

    def get_paths():
        i, j = source
        frontier = [((i, j, None),)]

        while True:
            new_frontier = []
            for path in frontier:
                node = path[-1]

                (i, j, _) = node
                if (i, j) == dest:
                    paths = [path for path in frontier if (path[-1][0], path[-1][1]) == dest]
                    return paths

                for neighbor in get_neighbors(node):
                    new_path = path + (neighbor,)
                    new_frontier.append(new_path)

            frontier = new_frontier

    paths = get_paths()

    def get_directions(path):
        directions = tuple(direction for (_, _, direction) in path[1:])
        directions += ('A',)
        return directions

    paths = [get_directions(path) for path in paths]

    return paths


def get_numeric_shortest_paths():
    numeric_pad_shortest_paths = {}
    for source, dest in list(itertools.product(NUMERIC_PAD.keys(), NUMERIC_PAD.keys())):
        numeric_pad_shortest_paths[(source, dest)] = get_shortest_numeric_paths(
            NUMERIC_PAD[source], NUMERIC_PAD[dest]
        )
    return numeric_pad_shortest_paths


NUMERIC_SHORTEST_PATHS = get_numeric_shortest_paths()


DIRECTIONAL_PAD = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

def get_shortest_directional_paths(source, dest):
    def get_neighbors(node):
        (i, j, _) = node

        neighbors = []
        if i-1 >= 0 and (i-1, j) != (0, 0):
            neighbor = (i-1, j, '^')
            neighbors.append(neighbor)

        if i+1 <= 1:
            neighbor = (i+1, j, 'v')
            neighbors.append(neighbor)

        if j-1 >= 0 and (i, j-1) != (0, 0):
            neighbor = (i, j-1, '<')
            neighbors.append(neighbor)

        if j+1 <= 2:
            neighbor = (i, j+1, '>')
            neighbors.append(neighbor)

        return neighbors

    def get_paths():
        i, j = source
        frontier = [((i, j, None),)]

        while True:
            new_frontier = []
            for path in frontier:
                node = path[-1]

                (i, j, _) = node
                if (i, j) == dest:
                    paths = [path for path in frontier if (path[-1][0], path[-1][1]) == dest]
                    return paths

                for neighbor in get_neighbors(node):
                    new_path = path + (neighbor,)
                    new_frontier.append(new_path)

            frontier = new_frontier

    paths = get_paths()

    def get_directions(path):
        directions = tuple(direction for (_, _, direction) in path[1:])
        directions += ('A',)
        return directions

    paths = [get_directions(path) for path in paths]

    return paths


def get_directional_shortest_paths():
    directional_pad_shortest_paths = {}
    for source, dest in list(itertools.product(DIRECTIONAL_PAD.keys(), DIRECTIONAL_PAD.keys())):
        directional_pad_shortest_paths[(source, dest)] = get_shortest_directional_paths(
            DIRECTIONAL_PAD[source], DIRECTIONAL_PAD[dest]
        )
    return directional_pad_shortest_paths


DIRECTIONAL_SHORTEST_PATHS = get_directional_shortest_paths()


def get_transitions(buttons):
    transitions = zip(['A']+list(buttons), buttons)
    return transitions


MEMO = {}
def get_length(button_sequence, depth):
    if depth == 0:
        return len(button_sequence)

    if (button_sequence, depth) in MEMO:
        return MEMO[(button_sequence, depth)]

    transitions = get_transitions(button_sequence)

    total_length = 0
    for start, end in transitions:
        directional_shortest_paths = DIRECTIONAL_SHORTEST_PATHS[(start, end)]

        min_length = float('inf')
        lengths = []
        for directional_shortest_path in directional_shortest_paths:
            length = get_length(directional_shortest_path, depth-1)
            lengths.append((start, end, directional_shortest_path, depth, length))
            min_length = min(length, min_length)

        total_length += min_length

    MEMO[(button_sequence, depth)] = total_length

    return total_length


def get_complexity(shortest_sequence_length, code):
    def get_numeric(code):
        numeric_str = ''.join(c for c in code if c.isdigit())
        numeric = int(numeric_str)
        return numeric

    complexity = shortest_sequence_length * get_numeric(code)
    return complexity


if __name__ == '__main__':
    codes = get_codes()

    complexities = []
    for code in codes:
        transitions = get_transitions(code)

        total_length = 0
        for start, end in transitions:
            numeric_shortest_paths = NUMERIC_SHORTEST_PATHS[(start, end)]

            min_length = float('inf')
            for numeric_shortest_path in numeric_shortest_paths:
                length = get_length(numeric_shortest_path, depth=25)
                min_length = min(length, min_length)

            total_length += min_length

        complexity = get_complexity(total_length, code)
        complexities.append(complexity)

    print(sum(complexities))

