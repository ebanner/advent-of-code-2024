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


def get_antinodes(a, b, grid):
    _, x1, y1 = a
    _, x2, y2 = b

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x1 < x2 and y2 > \
                   y1:
        antinodes = [(x1-dx, y1-dy), (x2+dx, y2+dy)]
    elif x1 < x2 and y1 > \
                     y2:
        antinodes = [(x1-dx, y1+dy), (x2+dx, y2-dy)]
    elif x2 < x1 and y1 > \
                     y2:
        antinodes = [(x1+dx, y1+dy), (x2-dx, y2-dy)]
    elif x2 < x1 and y2 > \
                     y1:
        antinodes = [(x1+dx, y1-dy), (x2-dx, y2+dy)]
    else:
        raise Exception(x1, y1, x2, y2)
        antinodes = []

    return antinodes


def get_all_antinodes(antennas, grid):
    n = len(grid)
    m = len(grid[0])

    for i in range(len(antennas)-1):
        for j in range(i+1, len(antennas)):
            a, _, _ = antennas[i]
            b, _, _ = antennas[j]
            if a != b:
                continue
            antinodes = get_antinodes(antennas[i], antennas[j], grid)
            for (x, y) in antinodes:
                i_ = n-y-1
                j_ = x
                if not (0 <= i_ < n and 0 <= j_ < m):
                    continue
                grid[i_][j_] = '#'
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

