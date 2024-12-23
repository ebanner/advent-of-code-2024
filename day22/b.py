import sys

from tqdm import tqdm


def get_initial_secret_numbers():
    initial_secret_numbers = [int(line.strip()) for line in sys.stdin.readlines()]
    return initial_secret_numbers


def step(secret_number):
    secret_number ^= secret_number << 6
    secret_number %= 16777216

    # print('1', secret_number)

    secret_number ^= secret_number >> 5
    secret_number %= 16777216

    # print('2', secret_number)

    secret_number ^= secret_number << 11
    secret_number %= 16777216

    # print('3', secret_number)

    return secret_number


def get_secret_numbers(initial_secret_number):
    secret_number = initial_secret_number

    secret_numbers = [secret_number]
    for _ in range(2000):
        secret_number = step(secret_number)
        secret_numbers.append(secret_number)

    return secret_numbers


def get_prices(secret_numbers):
    prices = []
    for secret_number in secret_numbers:
        price = secret_number % 10
        prices.append(price)
    return prices


def get_differences(prices):
    differences = [None]
    for i in range(1, len(prices)):
        difference = prices[i] - prices[i-1]
        differences.append(difference)
    return differences


def get_difference_window_prices(differences, prices):
    difference_window_prices = {}
    for i in range(4, len(prices)):
        difference_window = tuple(differences[i-3:i+1])
        if difference_window in difference_window_prices:
            continue
        difference_window_prices[difference_window] = prices[i]

    return difference_window_prices


def get_max_difference_window(difference_window_prices):
    max_price = -1
    max_difference_window = (None, None, None, None)

    for difference_window, total_price in difference_window_prices.items():
        if total_price > max_price:
            max_price = total_price
            max_difference_window = difference_window

    return max_difference_window


def combine(a, b):
    c = {}
    for difference_window, total_price in a.items():
        c[difference_window] = total_price

    for difference_window, price in b.items():
        if difference_window in c:
            c[difference_window] += price
        else:
            c[difference_window] = price

    return c


if __name__ == '__main__':
    initial_secret_numbers = get_initial_secret_numbers()

    prices = []
    differences= []
    difference_window_prices = {}
    for initial_secret_number in tqdm(initial_secret_numbers):
        secret_numbers = get_secret_numbers(initial_secret_number)

        prices_row = get_prices(secret_numbers)
        prices.append(prices_row)

        differences_row = get_differences(prices_row)
        differences.append(differences_row)

        difference_window_prices = combine(
            difference_window_prices,
            get_difference_window_prices(differences_row, prices_row)
        )

    max_difference_window = get_max_difference_window(difference_window_prices)

    print(difference_window_prices[max_difference_window])

