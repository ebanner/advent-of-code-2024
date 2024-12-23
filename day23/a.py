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


def get_computers(connections):
    computers = connections.keys()
    return computers


if __name__ == '__main__':
    connections = get_connections()
    computers = get_computers(connections)

    connected_triplets = get_connected_triplets(connections, computers)

    num_t = 0
    for (c1, c2, c3) in connected_triplets:
        if c1.startswith('t') or c2.startswith('t') or c3.startswith('t'):
            num_t += 1

    print(num_t)

