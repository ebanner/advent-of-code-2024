import sys


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


def get_count(quadrant):
    count = 0
    for i in range(len(quadrant)):
        for j in range(len(quadrant[0])):
            if quadrant[i][j] != '.':
                count += int(quadrant[i][j])
    return count


def count_quadrants(states):
    n = 103
    m = 101

    grid = get_grid(states)

    quadrants = [
        [row[:50] for row in grid[:51]],
        [row[51:] for row in grid[:51]],
        [row[:50] for row in grid[52:]],
        [row[51:] for row in grid[52:]],
    ]

    quadrant_counts = []
    for quadrant in quadrants:

        count = get_count(quadrant)
        quadrant_counts.append(count)

    return quadrant_counts
        


if __name__ == '__main__':
    states = get_positions_and_velocities()

    for _ in range(100):
        new_states = []
        for state in states:
            new_state = tick(state)
            new_states.append(new_state)

        states = new_states

    quadrant_counts = count_quadrants(new_states)

    quadrant_product = 1
    for quadrant_count in quadrant_counts:
        quadrant_product *= quadrant_count

    print(quadrant_product)
