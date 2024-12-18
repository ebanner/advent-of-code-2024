import sys


def get_bytes():
    lines = [line.strip() for line in sys.stdin.readlines()]

    bytes = []
    for line in lines:
        x, y = map(int, line.split(','))
        j, i = x, y
        byte = i, j
        bytes.append(byte)
    return bytes


def get_memory(size=7):
    memory = [['.']*size for _ in range(size)]
    return memory


def place_bytes(bytes, memory):
    for i, j in bytes:
        memory[i][j] = '#'
    return memory


def get_neighbors(node, memory):
    i, j = node

    n = len(memory)
    m = len(memory[0])

    neighbors = []
    if i > 0 and memory[i-1][j] != '#':
        neighbors.append((i-1, j))
    if j < m-1 and memory[i][j+1] != '#':
        neighbors.append((i, j+1))
    if i < n-1 and memory[i+1][j] != '#':
        neighbors.append((i+1, j))
    if j > 0 and memory[i][j-1] != '#':
        neighbors.append((i, j-1))

    return neighbors


def bfs(start, end, memory):
    frontier = [start]
    memory[0][0] = 'O'
    level = 0

    while frontier:
        new_frontier = []
        for node in frontier:
            if node == end:
                return level

            for neighbor in get_neighbors(node, memory):
                (i, j) = neighbor
                if memory[i][j] == 'O':
                    continue

                new_frontier.append(neighbor)
                memory[i][j] = 'O'

        frontier = new_frontier
        level += 1

    return -1


def copy(memory):
    memory_copy = [row[:] for row in memory]
    return memory_copy


if __name__ == '__main__':
    bytes = get_bytes()

    MEMORY_SIZE = 71

    n = MEMORY_SIZE
    m = MEMORY_SIZE

    start = (0, 0)
    end = (n-1, m-1)

    blank_memory = get_memory(MEMORY_SIZE)

    byte_idx = 1
    while True:
        memory = copy(blank_memory)
        bytes_slice = bytes[:byte_idx]
        memory = place_bytes(bytes_slice, memory)

        min_steps = bfs(start, end, memory)
        if min_steps == -1:
            (i, j) = bytes_slice[-1]
            (x, y) = (j, i)
            print(f'{x},{y}')
            exit(1)
            break

        byte_idx += 1

