import sys


def get_input():
    lines = [line for line in sys.stdin.readlines()]
    input_str = ''.join(lines).strip()
    return input_str


def parse_rules(rules_str):
    rules = {}
    for rule_str in rules_str.split('\n'):
        a, b = map(int, rule_str.split('|'))
        if a not in rules:
            rules[a] = []
        rules[a].append(b)
    return rules


def get_rules(input_str):
    rules_str, _ = input_str.split('\n\n')
    rules = parse_rules(rules_str)
    return rules


def parse_updates(updates_str):
    updates = []
    for update_str in updates_str.split('\n'):
        update = list(map(int, update_str.split(',')))
        updates.append(update)
    return updates


def get_updates(input_str):
    _, updates_str = input_str.split('\n\n')
    updates = parse_updates(updates_str)
    return updates


def is_valid(update, rules):
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if update[j] not in rules:
                continue
            pages = rules[update[j]]
            if update[i] in pages:
                return False
    return True


def get_midpoint(update):
    midpoint_idx = len(update) // 2
    return update[midpoint_idx]


def get_invalid_updates(updates, rules):
    invalid_updates = []
    for update in updates:
        if not is_valid(update, rules):
            invalid_updates.append(update)
    return invalid_updates


def try_fix(update, rules):
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if update[j] not in rules:
                continue
            pages = rules[update[j]]
            if update[i] in pages:
                update[i], update[j] = update[j], update[i]
    return update


if __name__ == '__main__':
    input_str = get_input()

    rules = get_rules(input_str)
    updates = get_updates(input_str)

    invalid_updates = get_invalid_updates(updates, rules)

    fixed_updates = []
    for update in invalid_updates:
        while not is_valid(update, rules):
            update = try_fix(update, rules)
        fixed_updates.append(update)

    midpoints = []
    for update in fixed_updates:
        midpoint = get_midpoint(update)
        midpoints.append(midpoint)

    print(sum(midpoints))
