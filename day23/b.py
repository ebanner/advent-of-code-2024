import sys

import itertools


def get_connections():
    def make_connections(connection_tuples):
        connections = {}

        def add(ca, cb):
            if ca not in connections:
                connections[ca] = []
            connections[ca].append(cb)

        for (c1, c2) in connection_tuples:
            add(c1, c2)
            add(c2, c1)
        return connections

    connection_strs = [line.strip() for line in sys.stdin.readlines()]

    connection_tuples = []
    for connection_str in connection_strs:
        connection_tuple = connection_str.split('-')
        connection_tuples.append(connection_tuple)

    connections = make_connections(connection_tuples)
    return connections


def get_triplets(computers):
    triplets = list(itertools.combinations(computers, 3))
    return triplets


def is_connected(triplet, connections):
    (c1, c2, c3) = triplet

    return (c2 in connections[c1] and c3 in connections[c1]) and \
            (c1 in connections[c2] and c3 in connections[c2]) and \
             (c1 in connections[c3] and c2 in connections[c3])


def get_connected_triplets(connections, computers):
    triplets = get_triplets(computers)

    connected_triplets = []
    for triplet in triplets:
        if is_connected(triplet, connections):
            connected_triplets.append(triplet)

    return connected_triplets


def get_largest_set(connections):
    largest_set = set()
    for computer, rest in connections.items():
        if len(rest)+1 > len(largest_set):
            pool = set(rest)
            pool.add(computer)
            largest_set = pool

    return largest_set


def get_password(set):
    password = ','.join(sorted(set))
    return password


def forms_a_clique(computer, clique, connections):
    def fully_connected(nodes, connections):
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                if nodes[j] not in connections[nodes[i]]:
                    return False
        return True

    return fully_connected(tuple(sorted((computer,) + clique)), connections)


def get_computers(connections):
    computers = list(connections.keys())
    return computers


def get_largest_clique(connections):
    computers = get_computers(connections)

    frontier = {(computer,) for computer in computers}

    clique_size = 1

    while True:
        new_frontier = set()
        for clique in frontier:
            for computer in computers:
                if forms_a_clique(computer, clique, connections):
                    new_clique = tuple(sorted((computer,) + clique))
                    new_frontier.add(new_clique)

        if not new_frontier:
            break

        frontier = new_frontier

        clique_size += 1

    max_clique = (computers[0],)
    for clique in frontier:
        if len(clique) > len(max_clique):
            max_clique = clique

    return max_clique


if __name__ == '__main__':
    connections = get_connections()

    largest_set = get_largest_clique(connections)

    password = get_password(largest_set)

    print(password)

