import sys

from tqdm import trange


def get_pebbles():
    pebbles = {int(num): 1 for num in sys.stdin.readline().split()}
    return pebbles


def split(pebble):
    split_pebbles = []
    pebble_str = str(pebble)
    pebble_length = len(pebble_str)
    pebbles = int(pebble_str[:pebble_length//2]), int(pebble_str[pebble_length//2:])
    return pebbles


def transform_pebble(pebble):
    if pebble == 0:
        new_pebbles = [1]
    elif len(str(pebble)) % 2 == 0:
        new_pebbles = split(pebble)
    else:
        new_pebbles = [pebble * 2024]
    return new_pebbles


def add(pebble, count, pebbles):
    if pebble not in pebbles:
        pebbles[pebble] = 0
    pebbles[pebble] += count


if __name__ == '__main__':
    pebbles = get_pebbles()
    for i in trange(75):
        new_pebbles = {}
        for pebble, count in pebbles.items():
            transformed_pebbles = transform_pebble(pebble)
            for transformed_pebble in transformed_pebbles:
                add(transformed_pebble, count, new_pebbles)
        pebbles = new_pebbles

    num_pebbles = 0
    for _, count in pebbles.items():
        num_pebbles += count
    print(num_pebbles)
