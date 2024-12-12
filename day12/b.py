import sys


def get_garden():
    garden = [list(line.strip()) for line in sys.stdin.readlines()]
    return garden


def get_zeros(garden):
    zeros = [[0]*len(row) for row in garden]
    return zeros


def get_num_convex_corners(i, j, garden):
    num_convex_corners = 0
    n = len(garden)
    m = len(garden[0])

    # upper left
    if (i == 0 or garden[i-1][j] != garden[i][j]) and (j == 0 or garden[i][j-1] != garden[i][j]):
        num_convex_corners += 1

    # top right
    if (i == 0 or garden[i-1][j] != garden[i][j]) and (j == m-1 or garden[i][j+1] != garden[i][j]):
        num_convex_corners += 1

    # bottom right
    if (j == m-1 or garden[i][j+1] != garden[i][j]) and (i == n-1 or garden[i+1][j] != garden[i][j]):
        num_convex_corners += 1

    # bottom left
    if (i == n-1 or garden[i+1][j] != garden[i][j]) and (j == 0 or garden[i][j-1] != garden[i][j]):
        num_convex_corners += 1

    return num_convex_corners


def get_num_concave_corners(i, j, garden):
    num_concave_corners = 0
    n = len(garden)
    m = len(garden[0])

    # upper right
    if (i > 0 and garden[i-1][j] == garden[i][j]) and (i > 0 and j < m-1 and garden[i-1][j+1] != garden[i][j]) and \
                                                     (j < m-1 and garden[i][j+1] == garden[i][j]):
        num_concave_corners += 1

    # bottom right
    if                                                  (j < m-1 and garden[i][j+1] == garden[i][j]) and \
       (i < n-1 and garden[i+1][j] == garden[i][j]) and (i < n-1 and j < m-1 and garden[i+1][j+1] != garden[i][j]):
        num_concave_corners += 1

    # bottom left
    if (j > 0 and garden[i][j-1] == garden[i][j]) and \
       (i < n-1 and j > 0 and garden[i+1][j-1] != garden[i][j]) and (i < n-1 and garden[i+1][j] == garden[i][j]):
        num_concave_corners += 1

    # top left
    if (i > 0 and j > 0 and garden[i-1][j-1] != garden[i][j]) and (i > 0 and garden[i-1][j] == garden[i][j]) and \
       (j > 0 and garden[i][j-1] == garden[i][j]):
        num_concave_corners += 1

    return num_concave_corners


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

    total_num_corners = 0
    total_area = 0
    for (i_, j_) in get_neighbors(i, j, garden):
        if visited[i_][j_]:
            continue

        num_corners, area = flood_fill(i_, j_, garden, visited)
        total_num_corners += num_corners
        total_area += area

    num_convex_corners = get_num_convex_corners(i, j, garden)
    num_concave_corners = get_num_concave_corners(i, j, garden)
    num_corners = num_convex_corners + num_concave_corners
    total_num_corners += num_corners
    total_area += 1

    return total_num_corners, total_area


if __name__ == '__main__':
    garden = get_garden()
    visited = get_zeros(garden)
    num_sides_list = []
    areas = []
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if visited[i][j] == 0:
                num_corners, area = flood_fill(i, j, garden, visited)
                num_sides_list.append(num_corners)
                areas.append(area)

    total_price = 0
    for num_sides, area in zip(num_sides_list, areas):
        price = num_sides * area
        total_price += price

    print(total_price)
