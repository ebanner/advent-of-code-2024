import sys


def get_garden():
    garden = [list(line.strip()) for line in sys.stdin.readlines()]
    return garden


def get_zeros(garden):
    zeros = [[0]*len(row) for row in garden]
    return zeros


def get_num_fence(i, j, garden):
    num_fence = 0
    n = len(garden)
    m = len(garden[0])

    # up
    if i == 0:
        num_fence += 1
    elif garden[i-1][j] != garden[i][j]:
        num_fence += 1

    # down
    if i == n-1:
        num_fence += 1
    elif garden[i+1][j] != garden[i][j]:
        num_fence += 1

    # left
    if j == 0:
        num_fence += 1
    elif garden[i][j-1] != garden[i][j]:
        num_fence += 1

    # right
    if j == m-1:
        num_fence += 1
    elif garden[i][j+1] != garden[i][j]:
        num_fence += 1

    return num_fence


def get_neighbors(i, j, garden):
    n = len(garden)
    m = len(garden[0])

    neighbors = []
    if i > 0 and garden[i-1][j] == garden[i][j]:
        neighbors.append((i-1, j))
    if i < n-1 and garden[i+1][j] == garden[i][j]:
        neighbors.append((i+1, j))
    if j > 0 and garden[i][j-1] == garden[i][j]:
        neighbors.append((i, j-1))
    if j < m-1 and garden[i][j+1] == garden[i][j]:
        neighbors.append((i, j+1))

    return neighbors


def flood_fill(i, j, garden, visited):
    visited[i][j] = 1

    total_num_fence = 0
    total_area = 0
    for (i_, j_) in get_neighbors(i, j, garden):
        if visited[i_][j_]:
            continue

        num_fence, area = flood_fill(i_, j_, garden, visited)
        total_num_fence += num_fence
        total_area += area

    total_num_fence += get_num_fence(i, j, garden)
    total_area += 1

    return total_num_fence, total_area


if __name__ == '__main__':
    garden = get_garden()
    visited = get_zeros(garden)
    num_fences = []
    areas = []
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if visited[i][j] == 0:
                num_fence, area = flood_fill(i, j, garden, visited)
                num_fences.append(num_fence)
                areas.append(area)

    total_price = 0
    for num_fence, area in zip(num_fences, areas):
        price = num_fence * area
        total_price += price

    print(total_price)
