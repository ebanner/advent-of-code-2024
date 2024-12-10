import sys


def get_map():
    my_map = [list(map(int, line.strip())) for line in sys.stdin.readlines()]
    return my_map


def get_trailheads(map):
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads


def get_neighbors(location, map):
    i, j = location
    height = map[i][j]

    neighbors = []
    if 0 <= i-1 and map[i-1][j] == height + 1:
        neighbors.append((i-1, j))

    if i+1 < len(map) and map[i+1][j] == height + 1:
        neighbors.append((i+1, j))

    if 0 <= j-1 and map[i][j-1] == height + 1:
        neighbors.append((i, j-1))

    if j+1 < len(map[0]) and map[i][j+1] == height + 1:
        neighbors.append((i, j+1))

    return neighbors


def dfs(location, map, visited):
    i, j = location
    if map[i][j] == 9:
        return 1

    neighbors = get_neighbors(location, map)
    total_score = 0
    for neighbor in neighbors:
        if neighbor in visited:
            continue
        visited.append(neighbor)
        score = dfs(neighbor, map, visited)
        total_score += score
    return total_score


if __name__ == '__main__':
    map = get_map()
    trailheads = get_trailheads(map)

    total_score = 0
    for trailhead in trailheads:
        score = dfs(trailhead, map, [])
        total_score += score

    print(total_score)
