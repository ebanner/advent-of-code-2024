import sys

import math

from tqdm import trange


def parse(position_and_velocity_str):
    position_str, velocity_str = position_and_velocity_str.split()

    _, position_str = position_str.split('=')
    x_str, y_str = position_str.split(',')
    x, y = int(x_str), int(y_str)

    _, velocity_str = velocity_str.split('=')
    dx_str, dy_str = velocity_str.split(',')
    dx, dy = int(dx_str), int(dy_str)

    return (x, y), (dx, dy)


def get_positions_and_velocities():
    position_and_velocities_strs = [line.strip() for line in sys.stdin.readlines()]

    position_and_veclocities = []
    for position_and_velocity_str in position_and_velocities_strs:
        position_and_velocity = parse(position_and_velocity_str)
        position_and_veclocities.append(position_and_velocity)

    return position_and_veclocities


def tick(state):
    n = 103
    m = 101

    (x, y), (dx, dy) = state

    x += dx
    x %= m

    y += dy
    y %= n

    return (x, y), (dx, dy)


def get_grid(states):
    n = 103
    m = 101

    grid = [[0]*m for _ in range(n)]

    for (x, y), _ in states:
        grid[y][x] += 1 

    for y in range(n):
        for x in range(m):
            if grid[y][x] == 0:
                grid[y][x] = '.'
            else:
                grid[y][x] = str(grid[y][x])

    return grid


def filter_sum(lens):
    sum = 0
    for i in range(len(lens)):
        for j in range(len(lens[0])):
            if lens[i][j] == '.':
                continue
            sum += 1
    return sum


def convole(states):
    grid = get_grid(states)
    sums = []
    for i in range(len(grid)-3):
        for j in range(len(grid[0])):
            s = filter_sum([grid[i+k][j:j+3] for k in range(3)])
            sums.append(s)
    return sum(sums) / len(sums)


if __name__ == '__main__':
    states = get_positions_and_velocities()

    max_score = convole(states)
    max_grid = get_grid(states)
    max_i = 0
    for i in trange(1, 10000+1):
        new_states = []
        for state in states:
            new_state = tick(state)
            new_states.append(new_state)
        states = new_states

        score = convole(states)
        if score > max_score:
            max_score = score
            max_grid = get_grid(states)
            max_i = i

    for row in max_grid:
        print(''.join(row))
    print()
    print(max_i)

