import sys


def get_initial_secret_numbers():
    initial_secret_numbers = [int(line.strip()) for line in sys.stdin.readlines()]
    return initial_secret_numbers


def step(secret_number):
    secret_number ^= secret_number << 6
    secret_number %= 16777216

    secret_number ^= secret_number >> 5
    secret_number %= 16777216

    secret_number ^= secret_number << 11
    secret_number %= 16777216

    return secret_number


def get_secret_number(initial_secret_number):
    secret_number = initial_secret_number

    for _ in range(2000):
        secret_number = step(secret_number)

    return secret_number


if __name__ == '__main__':
    initial_secret_numbers = get_initial_secret_numbers()

    secret_numbers = []
    for initial_secret_number in initial_secret_numbers:
        secret_number = get_secret_number(initial_secret_number)
        secret_numbers.append(secret_number)

    print(sum(secret_numbers))
