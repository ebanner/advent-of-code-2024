import sys

from tqdm import tqdm


def get_input():
    lines = [line for line in sys.stdin.readlines()]
    input = ''.join(lines)
    return input


def get_input_chunks(input):
    input_chunks = [input_chunk.strip() for input_chunk in input.split('\n\n')]
    return input_chunks


def getX(input_chunk):
    X = []

    machine1_str, machine2_str, _ = input_chunk.split('\n')
    _, xy_str = machine1_str.split(':')
    xplus_str, _ = xy_str.split(',')
    _, x_str =  xplus_str.split('+')
    x = int(x_str)
    X.append(x)

    _, xy_str = machine2_str.split(':')
    xplus_str, _ = xy_str.split(',')
    _, x_str =  xplus_str.split('+')
    x = int(x_str)
    X.append(x)

    return X


def getY(input_chunk):
    Y = []

    machine1_str, machine2_str, _ = input_chunk.split('\n')
    _, xy_str = machine1_str.split(':')
    _, yplus_str = xy_str.split(',')
    _, y_str =  yplus_str.split('+')
    y = int(y_str)
    Y.append(y)

    _, xy_str = machine2_str.split(':')
    _, yplus_str = xy_str.split(',')
    _, y_str =  yplus_str.split('+')
    y = int(y_str)
    Y.append(y)

    return Y


def get_prize(input_chunk):
    _, _, prize_str = input_chunk.split('\n')
    _, xy_str = prize_str.split(':')
    xplus_str, yplus_str = xy_str.split(',')
    (_, x_str), (_, y_str) = xplus_str.split('='), yplus_str.split('=')
    x, y = int(x_str), int(y_str)
    prize = x, y

    return prize


def get_min_cost(prizeX, prizeY, X, Y, memo, indent):
    A, B = 0, 1

    numerator = Y[A]*prizeX - prizeY*X[A]
    denominator = Y[A]*X[B] - Y[B]*X[A]

    if numerator % denominator == 0:
        b = numerator // denominator
        if (prizeX - X[B]*b) % X[A] != 0:
            return -1
        else:
            a = (prizeX - X[B]*b) // X[A]
            cost = 3*a + b
            return cost
    else:
        return -1


if __name__ == '__main__':
    input = get_input()
    input_chunks = get_input_chunks(input)

    total_min_cost = 0
    for input_chunk in tqdm(input_chunks):
        prizeX, prizeY = get_prize(input_chunk)
        prizeX += 10000000000000
        prizeY += 10000000000000
        X, Y = getX(input_chunk), getY(input_chunk)
        min_cost = get_min_cost(prizeX, prizeY, X, Y, {}, 0)
        if min_cost != -1:
            total_min_cost += min_cost

    print(total_min_cost)
