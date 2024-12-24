import sys 


def get_nodes():
    def get_input():
        lines = [line for line in sys.stdin.readlines()]
        input_str = ''.join(lines).strip()
        return input_str

    def parse_values(values_str):
        values = {}
        for value_str in values_str.split('\n'):
            name, value = value_str.split(':')
            values[name] = int(value)
        return values

    def get_values(input_str):
        values_str, _ = input_str.split('\n\n')
        values = parse_values(values_str)
        return values

    def parse_rules(rules_str):
        rules = []
        for rule_str in rules_str.split('\n'):
            input, output = rule_str.split('->')
            input1, operation, input2 = input.split()
            output = output.strip()
            rule = (input1, operation, input2, output)
            rules.append(rule)
        return rules

    def get_rules(input_str):
        _, rules_str = input_str.split('\n\n')
        rules = parse_rules(rules_str)
        return rules

    input_str = get_input()
    values = get_values(input_str)
    rules = get_rules(input_str)

    nodes = {}
    for name, value in values.items():
        node = [name, None, value, [], []]
        nodes[name] = node

    OUTPUT = 4
    for (input1, operation, input2, output) in rules:
        if input1 not in nodes:
            nodes[input1] = [input1, None, None, [], []]
        nodes[input1][OUTPUT].append(output)

        if input2 not in nodes:
            nodes[input2] = [input2, None, None, [], []]
        nodes[input2][OUTPUT].append(output)

        if output not in nodes:
            node = [output, operation, None, [input1, input2], []]
            nodes[output] = node

        OPERATION = 1
        INPUTS = 3
        nodes[output][OPERATION] = operation
        nodes[output][INPUTS] = [input1, input2]

    return nodes


def get_ordering(nodes):
    def dfs(node, ordering, visited):
        NAME = 0
        visited.append(node[NAME])

        OUTPUTS = 4
        for output in node[OUTPUTS]:
            if output not in visited:
                output_node = nodes[output]
                ordering, visited = dfs(output_node, ordering, visited)

        ordering = [node[NAME]] + ordering

        return ordering, visited

    total_ordering = []
    visited = []
    for name, node in nodes.items():
        if name not in visited:
            ordering = []
            ordering, visited = dfs(node, ordering, visited)
            total_ordering = ordering + total_ordering

    return total_ordering


def evaluate(ordering, nodes):
    def apply(operation, inputs):
        (x, y) = inputs
        if operation == 'AND':
            return x & y
        elif operation == 'OR':
            return x | y
        else:
            assert operation == 'XOR'
            return x ^ y

    for name in ordering:
        node = nodes[name]
        (_, operation, value, inputs, _) = node
        if value != None:
            continue

        VALUE = 2
        input_nodes = [nodes[input] for input in inputs]
        input_values = [input_node[VALUE] for input_node in input_nodes]

        value = apply(operation, input_values)

        nodes[name][VALUE] = value

    return nodes


if __name__ == '__main__':
    nodes = get_nodes()

    ordering = get_ordering(nodes)

    nodes = evaluate(ordering, nodes)

    def get_z_nodes(nodes):
        z_nodes = [node for name, node in nodes.items() if name.startswith('z')]
        return z_nodes

    VALUE = 2
    z_nodes = get_z_nodes(nodes)
    z_binary_sum = ''.join(str(node[VALUE]) for node in reversed(sorted(z_nodes)))
    z_decimal_sum = int(z_binary_sum, 2)

    print(z_decimal_sum)

