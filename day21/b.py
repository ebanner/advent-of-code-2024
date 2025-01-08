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


def get_numeric_shortest_paths():
    def get_how_numeric(source, dest):
        (i_start, j_start) = NUMERIC_PAD[source]
        (i_end, j_end) = NUMERIC_PAD[dest]

        di = i_end-i_start
        dj = j_end-j_start

        if dj < 0:
            j_how = ['<' for _ in range(-dj)]
        else:
            j_how = ['>' for _ in range(dj)]

        if di < 0:
            i_how = ['^' for _ in range(-di)]
        else:
            i_how = ['v' for _ in range(di)]


        if di < 0:
            how = i_how + j_how
        else:
            how = j_how + i_how

        how += ['A']

        return how

    numeric_pad_shortest_paths = {}
    for pair in list(itertools.product(NUMERIC_PAD.keys(), NUMERIC_PAD.keys())):
        numeric_pad_shortest_paths[pair] = get_how_numeric(*pair)
    return numeric_pad_shortest_paths


NUMERIC_SHORTEST_PATHS = get_numeric_shortest_paths()


DIRECTIONAL_PAD = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

def get_directional_shortest_paths():
    def get_how_directional(source, dest):
        (i_start, j_start) = DIRECTIONAL_PAD[source]
        (i_end, j_end) = DIRECTIONAL_PAD[dest]

        di = i_end-i_start
        dj = j_end-j_start

        if dj < 0:
            j_how = ['<' for _ in range(-dj)]
        else:
            j_how = ['>' for _ in range(dj)]

        if di < 0:
            i_how = ['^' for _ in range(-di)]
        else:
            i_how = ['v' for _ in range(di)]

        if di < 0:
            how = j_how + i_how
        else:
            how = i_how + j_how

        how += 'A'

        return how

    directional_pad_shortest_paths = {}
    for pair in list(itertools.product(DIRECTIONAL_PAD.keys(), DIRECTIONAL_PAD.keys())):
        directional_pad_shortest_paths[pair] = get_how_directional(*pair)
    return directional_pad_shortest_paths


DIRECTIONAL_SHORTEST_PATHS = get_directional_shortest_paths()


def get_transitions(buttons):
    transitions = zip(['A']+list(buttons), buttons)
    return transitions


def get_length(button_sequence, depth):
    if depth == 0:
        return len(button_sequence)

    transitions = get_transitions(button_sequence)

    total_length = 0
    for start, end in transitions:
        directional_shortest_path = DIRECTIONAL_SHORTEST_PATHS[(start, end)]

        length = get_length(directional_shortest_path, depth-1)
        total_length += length

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
            numeric_shortest_path = NUMERIC_SHORTEST_PATHS[(start, end)]

            length = get_length(numeric_shortest_path, depth=2)
            total_length += length

        print(code, total_length)

        complexity = get_complexity(total_length, code)
        complexities.append(complexity)

    print(sum(complexities))

