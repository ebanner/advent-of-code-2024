import sys


def get_grid():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    return grid


def get_antennas(grid):
    antennas = []
    n = len(grid)
    m = len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue
            x, y = j, n-i-1
            antenna = (grid[i][j], x, y)
            antennas.append(antenna)
    return antennas


def mark_antinodes(a, b, grid):
    _, x1, y1 = a
    _, x2, y2 = b

    dx = x2 - x1
    dy = y2 - y1

    x = x1
    y = y1

    while True:
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            break

        i = len(grid)-y-1
        j = x
        grid[i][j] = '#'

        x += dx
        y += dy

    x = x1
    y = y1

    while True:
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            break

        i = len(grid)-y-1
        j = x
        grid[i][j] = '#'

        x -= dx
        y -= dy


def get_all_antinodes(antennas, grid):
    n = len(grid)
    m = len(grid[0])

    for i in range(len(antennas)-1):
        for j in range(i+1, len(antennas)):
            a, _, _ = antennas[i]
            b, _, _ = antennas[j]
            if a != b:
                continue
            mark_antinodes(antennas[i], antennas[j], grid)
    return grid


def get_num_antinodes(grid):
    num_antinodes = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                num_antinodes += 1
    return num_antinodes


if __name__ == '__main__':
    grid = get_grid()
    antennas = get_antennas(grid)
    grid = get_all_antinodes(antennas, grid)

    num_antinodes = get_num_antinodes(grid)

    print(num_antinodes)

