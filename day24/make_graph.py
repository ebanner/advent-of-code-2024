import sys

from graphviz import Digraph


graph = Digraph("logic_graph")


def get_rules():
    def get_rule(line):
        x, op, y, _, z = line.split()
        rule = (x, y, op, z)
        return rule

    lines = [line.strip() for line in sys.stdin.readlines()]
    rules = [get_rule(line) for line in lines]
    return rules


def add_nodes(rules):
    nodes = {}
    for rule in rules:
        x, y, op, z = rule
        node_name = f'{op}_{x}_{y}'
        graph.node(node_name, label=op)
        nodes[z] = node_name
    return nodes


def add_edges(nodes, rules):
    for rule in rules:
        x, y, op, z = rule
        node_name = f'{op}_{x}_{y}'
        graph.edge(nodes.get(x, x), node_name, label=x)
        graph.edge(nodes.get(y, y), node_name, label=y)


def get_terminal_edges(rules):
    def get_edges(rules):
        edges = set()
        for rule in rules:
            x, y, _, z = rule
            edges.add(x)
            edges.add(y)
            edges.add(z)
        return edges

    def is_terminal(edge, rules):
        for rule in rules:
            x, y, _, _ = rule
            if edge == x or edge == y:
                return False
        return True

    edges = get_edges(rules)
    terminal_edges = []
    for edge in edges:
        if is_terminal(edge, rules):
            terminal_edge = edge
            terminal_edges.append(terminal_edge)

    return terminal_edges


def add_terminal_edges(terminal_edges, nodes):
    for terminal_edge in terminal_edges:
        graph.edge(nodes[terminal_edge], terminal_edge, label=terminal_edge)


if __name__ == '__main__':
    rules = get_rules()

    nodes = add_nodes(rules)
    add_edges(nodes, rules)

    terminal_edges = get_terminal_edges(rules)
    add_terminal_edges(terminal_edges, nodes)

    graph.render("logic_graph", format="png", cleanup=True)

