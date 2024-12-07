import sys


def get_input():
    input_lines = [line.strip() for line in sys.stdin.readlines()]
    return input_lines


def get_operands(input_lines):
    operands_list = []
    for line in input_lines:
        _, operands_str = line.split(':')
        operands_str = operands_str.strip()
        operands = list(map(int, operands_str.split()))
        operands_list.append(operands)
    return operands_list


def get_test_values(input_lines):
    test_values = []
    for line in input_lines:
        test_value, _ = line.split(':')
        test_values.append(int(test_value))
    return test_values


def apply(operators, operands):
    result = operands[0]
    i = 1
    j = 0
    while i < len(operands):
        if operators[j] == '+':
            result += operands[i]
        elif operators[j] == '*':
            result *= operands[i]
        else:
            raise Exception
        i += 1
        j += 1
    return result


def yields(test_value, operands, operators):
    if len(operators) == len(operands)-1:
        result = apply(operators, operands)
        if result == test_value:
            return True
        else:
            return False

    return yields(test_value, operands, operators + ['*']) or \
            yields(test_value, operands, operators + ['+'])


if __name__ == '__main__':
    input_lines = get_input()

    operands_list = get_operands(input_lines)
    test_values = get_test_values(input_lines)

    sum = 0
    for test_value, operands in zip(test_values, operands_list):
        if yields(test_value, operands, []):
            sum += test_value

    print(sum)
