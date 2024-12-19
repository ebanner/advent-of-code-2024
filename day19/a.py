from aoc import get_input


def get_towel_patterns(input_str):
    towel_patterns_str, _ = input_str.split('\n\n')
    towel_patterns = [towel_pattern.strip() for towel_pattern in towel_patterns_str.split(',')]
    return towel_patterns


def get_desired_designs(input_str):
    _, desired_designs_str = input_str.split('\n\n')
    desired_designs_str = desired_designs_str.strip()
    desired_designs = desired_designs_str.split('\n')
    return desired_designs


def is_possible(desired_design, towel_patterns):
    if desired_design == '':
        return True

    for towel_pattern in towel_patterns:
        if desired_design.startswith(towel_pattern):
            rest = desired_design[len(towel_pattern):]
            if is_possible(rest, towel_patterns):
                return True
    return False


if __name__ == '__main__':
    input_str = get_input()
    towel_patterns = get_towel_patterns(input_str)
    towel_patterns = list(reversed(sorted(towel_patterns, key=len)))
    desired_designs = get_desired_designs(input_str)

    num_possible = 0
    for desired_design in desired_designs:
        if is_possible(desired_design, towel_patterns):
            num_possible += 1

    print(num_possible)

