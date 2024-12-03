import re
import sys


def get_memory():
    lines = [line.strip() for line in sys.stdin.readline()]
    memory = ''.join(lines)
    return memory


def get_products(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory)

    products = []
    for match in matches:
        a, b = match
        product = int(a) * int(b)
        products.append(product)

    return products


if __name__ == '__main__':
    memory = get_memory()
    products = get_products(memory)
    result = sum(products)
    print(result)
