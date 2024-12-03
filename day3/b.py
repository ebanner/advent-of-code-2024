import re
import sys


def get_memory():
    lines = [line.strip() for line in sys.stdin]
    memory = ''.join(lines)
    return memory


def clean(memory):
    STATE = 'do'
    i = 0
    cleaned_memory = []
    while i < len(memory):
        if memory[i:i+7] == "don't()":
            STATE = "don't"
            i += 7
            continue
        elif memory[i:i+4] == 'do()':
            STATE = 'do'
            i += 4
            continue

        if STATE == "don't":
            i += 1
            continue

        cleaned_memory.append(memory[i])
        i += 1
    cleaned_memory = ''.join(cleaned_memory)
    return cleaned_memory


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
    clean_memory = clean(memory)
    products = get_products(clean_memory)
    result = sum(products)
    print(result)
