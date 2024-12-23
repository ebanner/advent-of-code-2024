import sys


def get_codes():
    codes = [line.strip() for line in sys.stdin.readlines()]
    return codes


def press(button, state):
    directional = [
       [None, '^', 'A'],
       [ '<', 'v', '>']
    ]

    numeric = [
        ['7',  '8', '9'],
        ['4',  '5', '6'],
        ['1',  '2', '3'],
        [None, '0', 'A'],
    ]

    def get_directional(elem):
        for i in range(len(directional)):
            for j in range(len(directional[0])):
                if directional[i][j] == elem:
                    return (i, j)

    def get_numeric(elem):
        for i in range(len(numeric)):
            for j in range(len(numeric[0])):
                if numeric[i][j] == elem:
                    return (i, j)

    (dpad1, dpad2, npad) = state

    (i1, j1) = get_directional(dpad1)

    new_dpad1 = dpad1
    new_dpad2 = dpad2
    new_npad = npad

    if button == '^':
        if i1 == 0 or directional[i1-1][j1] == None:
            return None
        new_dpad1 = directional[i1-1][j1]

    elif button == '<':
        if j1 == 0 or directional[i1][j1-1] == None:
            return None
        new_dpad1 = directional[i1][j1-1]

    elif button == '>':
        if j1 == 2:
            return None
        new_dpad1 = directional[i1][j1+1]

    elif button == 'v':
        if i1 == 1:
            return None
        new_dpad1 = directional[i1+1][j1]

    if button == 'A':

        button1 = dpad1

        (i2, j2) = get_directional(dpad2)

        if button1 == '^':
            if i2 == 0 or directional[i2-1][j2] == None:
                return None
            new_dpad2 = directional[i2-1][j2]

        elif button1 == '<':
            if j2 == 0 or directional[i2][j2-1] == None:
                return None
            new_dpad2 = directional[i2][j2-1]

        elif button1 == '>':
            if j2 == 2:
                return None
            new_dpad2 = directional[i2][j2+1]

        elif button1 == 'v':
            if i2 == 1:
                return None
            new_dpad2 = directional[i2+1][j2]

        if button1 == 'A':

            button2 = dpad2

            (i, j) = get_numeric(npad)

            if button2 == '^':
                if i == 0:
                    return None
                new_npad = numeric[i-1][j]

            elif button2 == '>':
                if j == 2:
                    return None
                new_npad = numeric[i][j+1]

            elif button2 == 'v':
                if i == 3 or numeric[i+1][j] == None:
                    return None
                new_npad = numeric[i+1][j]

            elif button2 == '<':
                if j == 0 or numeric[i][j-1] == None:
                    return None
                new_npad = numeric[i][j-1]

            elif button2 == 'A':
                pass

    return (new_dpad1, new_dpad2, new_npad)


def bfs(state, end):
    def get_neighbors(node):
        neighbors = []
        for button in [
                '^', 'A',
           '<', 'v', '>'
        ]:
            neighbor = press(button, node)
            if neighbor:
                neighbors.append(neighbor)
        return neighbors

    visited = {state: None}
    frontier = [state]

    while True:
        if frontier == []:
            break

        new_frontier = []
        for node in frontier:
            neighbors = get_neighbors(node, visited)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue

                visited[neighbor] = node
                if neighbor == end:
                    return visited

                new_frontier.append(neighbor)

        frontier = new_frontier

    return visited


def get_path(visited, start, end):
    node = start
    path = [node]
    while True:
        if node == end:
            break
        node = visited[node]
        path.append(node)
    return path


def recover_button_presses(path):
    button_presses = []
    for i, state in enumerate(path[:-1]):
        for button in [
                '^', 'A',
            '<', 'v', '>'
        ]:
            new_state = press(button, state)
            if new_state == path[i+1]:
                button_presses.append(button)
    button_presses += ['A']
    return button_presses


def get_fewest_button_presses(code):
    state = ('A', 'A', 'A')

    fewest_button_presses = []
    for c in code:
        end = ('A', 'A', c)

        visited = bfs(state, end)
        reversed_path = get_path(visited, start=end, end=state)
        path = list(reversed(reversed_path))
        button_presses = recover_button_presses(path)

        fewest_button_presses.append(button_presses)
        state = end

    return fewest_button_presses


def get_complexity(shortest_button_presses, code):
    def get_numeric(code):
        numeric_str = ''.join(c for c in code if c.isdigit())
        numeric = int(numeric_str)
        return numeric

    complexity = len(shortest_button_presses) * get_numeric(code)
    return complexity


if __name__ == '__main__':
    codes = get_codes()

    complexities = []
    for code in codes:
        fewest_button_presses_block = get_fewest_button_presses(code)

        fewest_button_presses = []
        for row in fewest_button_presses_block:
            fewest_button_presses.extend(row)

        complexity = get_complexity(fewest_button_presses, code)
        complexities.append(complexity)

    print(sum(complexities))
