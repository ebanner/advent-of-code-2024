import sys


def get_input():
    input_str = ''.join(sys.stdin.readlines()).strip()
    return input_str


def get_heights(grid_str):
    heights = [0, 0, 0, 0, 0]
    lines = grid_str.split('\n')

    for line in lines[1:-1]:
        for i in range(5):
            if line[i] == '#':
                heights[i] += 1

    return heights


def is_key(grid_str):
    lines = grid_str.split('\n')
    return all(char == '#' for char in lines[-1] )


def is_lock(grid_str):
    lines = grid_str.split('\n')
    return all(char == '#' for char in lines[0] )


def get_keys(input_str):
    grid_strs = input_str.split('\n\n')

    keys = []
    for grid_str in grid_strs:
        if not is_key(grid_str):
            continue
        key = get_heights(grid_str)
        keys.append(key)

    return keys


def get_locks(input_str):
    grid_strs = input_str.split('\n\n')

    locks = []
    for grid_str in grid_strs:
        if not is_lock(grid_str):
            continue
        lock = get_heights(grid_str)
        locks.append(lock)

    return locks


def fits_with(key, lock):
    for key_height, lock_height in zip(key, lock):
        if key_height + lock_height > 5:
            return False
    return True


if __name__ == '__main__':
    input_str = get_input()

    keys = get_keys(input_str)
    locks = get_locks(input_str)

    num_fit = 0
    for key in keys:
        for lock in locks:
            if fits_with(key, lock):
                num_fit += 1

    print(num_fit)

