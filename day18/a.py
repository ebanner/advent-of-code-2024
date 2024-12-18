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


def get_memory(bytes, size=7):
    memory = [['.']*size for _ in range(size)]
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

    while True:

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


if __name__ == '__main__':
    bytes = get_bytes()
    bytes = bytes[:1024]

    memory = get_memory(bytes, size=71)

    n = len(memory)
    m = len(memory[0])

    start = (0, 0)
    end = (n-1, m-1)
    min_steps = bfs(start, end, memory)

    print(min_steps)
