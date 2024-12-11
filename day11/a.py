import sys

from tqdm import trange


def get_pebbles():
    pebbles = [int(num) for num in sys.stdin.readline().split()]
    return pebbles


def split(pebble):
    split_pebbles = []
    pebble_str = str(pebble)
    pebble_length = len(pebble_str)
    pebbles = int(pebble_str[:pebble_length//2]), int(pebble_str[pebble_length//2:])
    return pebbles


def blink(pebbles):
    new_pebbles = []
    for pebble in pebbles:
        if pebble == 0:
            new_pebble = 1
            new_pebbles.append(new_pebble)
        elif len(str(pebble)) % 2 == 0:
            split_pebbles = split(pebble)
            new_pebbles.extend(split_pebbles)
        else:
            new_pebble = pebble * 2024
            new_pebbles.append(new_pebble)
    return new_pebbles


if __name__ == '__main__':
    pebbles = get_pebbles()
    for i in trange(75):
        pebbles = blink(pebbles)
        print(i, len(pebbles))

    print(len(pebbles))
