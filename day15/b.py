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
    instructions = ''.join(instructions_str.strip().split('\n'))
    return instructions


def double(map):
    chonk_map = []
    for row in map:
        new_row = []
        for elem in row:
            if elem == '#':
                new_row.extend(['#', '#'])
            elif elem == 'O':
                new_row.extend(['[', ']'])
            elif elem == '.':
                new_row.extend(['.', '.'])
            elif elem == '@':
                new_row.extend(['@', '.'])
        chonk_map.append(new_row)
    return chonk_map


def get_position(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                return i, j


def get_boxes(i, j, instruction, map):
    if instruction == '<':
        if map[i][j-1] == ']':
            box = (i, j-2)
            return box
        else:
            return None

    elif instruction == '^':
        boxes = []
        if map[i-1][j-1] == '[':
            box = (i-1, j-1)
            boxes.append(box)
        if map[i-1][j] == '[':
            box = (i-1, j)
            boxes.append(box)
        if map[i-1][j+1] == '[':
            box = (i-1, j+1)
            boxes.append(box)
        return boxes

    if instruction == '>':
        if map[i][j+2] == '[':
            box = (i, j+2)
            return box
        else:
            return None

    elif instruction == 'v':
        boxes = []
        if map[i+1][j-1] == '[':
            box = (i+1, j-1)
            boxes.append(box)
        if map[i+1][j] == '[':
            box = (i+1, j)
            boxes.append(box)
        if map[i+1][j+1] == '[':
            box = (i+1, j+1)
            boxes.append(box)
        return boxes


def get_gps_coordinates_sum(map):
    gps_coordinates_sum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '[':
                gps_coordinates_sum += 100*i + j
    return gps_coordinates_sum


get_box = get_boxes

def can_move(i, j, instruction, map, indent=0, do_move=False):
    n = len(map)
    m = len(map[0])

    if instruction == '<':
        if map[i][j-1] == '#':
            return False

        if not do_move:
            box = get_box(i, j, '<', map)
            if box:
                (box_i, box_j) = box
                if not can_move(box_i, box_j, '<', map, indent+2, do_move):
                    return False

        if do_move:
            box = get_box(i, j, '<', map)
            if box:
                (box_i, box_j) = box
                move(box_i, box_j, '<', map, do_move=True)

            map[i][j-1:j+1] = list('[]')
            map[i][j+1] = '.'

    elif instruction == '>':
        if map[i][j+2] == '#':
            return False

        box = get_box(i, j, '>', map)
        if box:
            (box_i, box_j) = box
            if not can_move(box_i, box_j, '>', map, indent+2, do_move):
                return False

        if do_move:
            box = get_box(i, j, '>', map)
            if box:
                (box_i, box_j) = box
                move(box_i, box_j, '>', map, do_move=True)

            map[i][j+1:j+3] = list('[]')
            map[i][j] = '.'

    elif instruction == 'v':
        if map[i+1][j] == '#' or map[i+1][j+1] == '#':
            return False

        if not do_move:
            for (box_i, box_j) in get_boxes(i, j, 'v', map):
                if not can_move(box_i, box_j, 'v', map, indent+2, do_move):
                    return False

        if do_move:
            for (box_i, box_j) in get_boxes(i, j, 'v', map):
                move(box_i, box_j, 'v', map, indent+2, do_move)

            map[i][j:j+2] = list('..')
            map[i+1][j:j+2] = list('[]')

    elif instruction == '^':
        if map[i-1][j] == '#' or map[i-1][j+1] == '#':
            return False

        if not do_move:
            for (box_i, box_j) in get_boxes(i, j, '^', map):
                if not can_move(box_i, box_j, '^', map, indent+2, do_move):
                    return False

        if do_move:
            for (box_i, box_j) in get_boxes(i, j, '^', map):
                move(box_i, box_j, '^', map, indent+2, do_move)

            map[i-1][j:j+2] = list('[]')
            map[i][j:j+2] = list('..')

    return True


move = can_move

def execute(instruction, map):
    position = get_position(map)

    i, j = position

    if instruction == '<':
        if map[i][j-1] == '#':
            pass

        if map[i][j-1] == ']':
            if can_move(i, j-2, '<', map):
                move(i, j-2, '<', map, do_move=True)

        if map[i][j-1] == '.':
            map[i][j-1:j+1] = list('@.')

    elif instruction == '>':
        if map[i][j+1] == '#':
            pass

        if map[i][j+1] == '[':
            if can_move(i, j+1, '>', map):
                move(i, j+1, '>', map, do_move=True)

        if map[i][j+1] == '.':
            map[i][j:j+2] = list('.@')

    elif instruction == '^':
        if map[i-1][j] == '#':
            pass

        if map[i-1][j] == '[':
            if can_move(i-1, j, '^', map):
                move(i-1, j, '^', map, do_move=True)

        elif map[i-1][j] == ']':
            if can_move(i-1, j-1, '^', map):
                move(i-1, j-1, '^', map, do_move=True)

        if map[i-1][j] == '.':
            map[i-1][j] = '@'
            map[i][j] = '.'

    elif instruction == 'v':
        if map[i+1][j] == '#':
            pass

        if map[i+1][j] == '[':
            if can_move(i+1, j, 'v', map):
                move(i+1, j, 'v', map, do_move=True)

        if map[i+1][j] == ']':
            if can_move(i+1, j-1, 'v', map):
                move(i+1, j-1, 'v', map, do_move=True)

        if map[i+1][j] == '.':
            map[i][j] = '.'
            map[i+1][j] = '@'

    return map


if __name__ == '__main__':
    input_str = get_input()
    map, instructions = get_map(input_str), get_instructions(input_str)
    chonk_map = double(map)

    for instruction in instructions:
        chonk_map = execute(instruction, chonk_map)

    gps_coordinates_sum = get_gps_coordinates_sum(chonk_map)
    print(gps_coordinates_sum)
