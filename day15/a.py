import sys


def get_input():
    lines = [line for line in sys.stdin.readlines()]
    input_str = ''.join(lines)
    return input_str


def get_map(input_str):
    map_str, _ = input_str.split('\n\n')
    map = [list(line) for line in map_str.split('\n')]
    return map


def get_instructions(input_str):
    _, instructions_str = input_str.split('\n\n')

    instructions = ''.join(instructions_str.strip())

    print('instructions', instructions)

    return instructions


def get_position(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                return i, j


def get_gps_coordinates(map):
    return [0]


def try_move(i, j, instruction, map):
    n = len(map)
    m = len(map[0])

    if instruction == '>':
        k = j+1
        while True:
            if k == m:
                return map

            if map[i][k] == '#':
                return map

            if map[i][k] == '.':
                map[i][j+2:k+1] = ['O']*(k-j-1)
                map[i][j], map[i][j+1] = '.', '@'
                return map

            assert map[i][k] == 'O'
            k += 1

    elif instruction == 'v':
        k = i+2
        while True:
            if k == n:
                return map

            if map[k][j] == '#':
                return map

            if map[k][j] == '.':
                for l in range(i+2, k+1):
                    map[l][j] = 'O'
                map[i][j] = '.'
                map[i+1][j] = '@'
                return map

            assert map[k][j] == 'O'
            k += 1

    elif instruction == '<':
        k = j-2
        while True:
            if k < 0:
                return map

            if map[i][k] == '#':
                return map

            if map[i][k] == '.':
                map[i][k:j-1] = 'O'
                map[i][j-1], map[i][j] = '@.'
                return map

            assert map[i][k] == 'O'
            k -= 1

    elif instruction == '^':
        raise NotImplementedError('^', 'try_move')


def execute(instruction, map):
    i, j = get_position(map)

    if instruction == '<':
        if map[i][j-1] == '#':
            pass
        elif map[i][j-1] == '.':
            map[i][j-1], map[i][j]  = '@', '.'
        elif map[i][j-1] == 'O':
            map = try_move(i, j, '<', map)
    elif instruction == '^':
        if map[i-1][j] == '#':
            raise NotImplementedError('^', '#')
        elif map[i-1][j] == '.':
            map[i-1][j] = '@'
            map[i][j] = '.'
        elif map[i-1][j] == 'O':
            raise NotImplementedError('^', 'O')
    elif instruction == '>':
        if map[i][j+1] == '#':
            raise NotImplementedError('>', '#')
        elif map[i][j+1] == '.':
            raise NotImplementedError('>', '.')
        elif map[i][j+1] == 'O':
            map = try_move(i, j, '>', map)
    elif instruction == 'v':
        if map[i+1][j] == '#':
            raise NotImplementedError('v', '#')
        elif map[i+1][j] == '.':
            map[i][j] = '.'
            map[i+1][j] = '@'
        elif map[i+1][j] == 'O':
            map = try_move(i, j, 'v', map)

    return map


if __name__ == '__main__':
    input_str = get_input()
    map, instructions = get_map(input_str), get_instructions(input_str)

    print(instructions)

    for row in map:
        print(''.join(row))
    print()

    for instruction in instructions:
        map = execute(instruction, map)

        print(f'Move {instruction}:')
        for row in map:
            print(''.join(row))
        print()

    gps_coordinates = get_gps_coordinates(map)
    print(sum(gps_coordinates))
