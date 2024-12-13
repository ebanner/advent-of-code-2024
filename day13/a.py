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
    if prizeX < 0 or prizeY < 0:
        return -1, memo

    if prizeX == 0 and prizeY == 0:
        memo[(prizeX, prizeY)] = 0
        return 0, memo

    if (prizeX, prizeY) in memo:
        return memo[(prizeX, prizeY)], memo

    min_cost = -1

    cost, memo = get_min_cost(prizeX-X[0], prizeY-Y[0], X, Y, memo, indent+2)
    if cost != -1:
        min_cost = min(min_cost, cost)+3 if min_cost != -1 else cost+3

    cost, memo = get_min_cost(prizeX-X[1], prizeY-Y[1], X, Y, memo, indent+2)
    if cost != -1:
        min_cost = min(min_cost, cost)+1 if min_cost != -1 else cost+1

    memo[(prizeX, prizeY)] = min_cost

    return min_cost, memo


if __name__ == '__main__':
    input = get_input()
    input_chunks = get_input_chunks(input)

    total_min_cost = 0
    for input_chunk in tqdm(input_chunks):
        prizeX, prizeY = get_prize(input_chunk)
        X, Y = getX(input_chunk), getY(input_chunk)
        min_cost, _ = get_min_cost(prizeX, prizeY, X, Y, {}, 0)
        if min_cost != -1:
            total_min_cost += min_cost

    print(total_min_cost)
