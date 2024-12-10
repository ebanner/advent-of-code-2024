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


def get_peaks(map):
    peaks = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 9:
                peaks.append((i, j))
    return peaks


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


def copy(visited):
    return visited[:]


def get_num_paths(location, peak, map, visited):
    if location == peak:
        return 1

    neighbors = get_neighbors(location, map)
    total_num_paths = 0
    for neighbor in neighbors:
        path_visited = copy(visited)
        if neighbor in path_visited:
            continue
        path_visited.append(neighbor)
        num_paths = get_num_paths(neighbor, peak, map, path_visited)
        total_num_paths += num_paths
    return total_num_paths


if __name__ == '__main__':
    map = get_map()
    trailheads = get_trailheads(map)
    peaks = get_peaks(map)

    ratings_sum = 0
    for trailhead in trailheads:
        for peak in peaks:
            rating = get_num_paths(trailhead, peak, map, [])
            ratings_sum += rating

    print(ratings_sum)
