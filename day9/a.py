import sys


def get_files():
    line = sys.stdin.readline().strip()
    files = []
    for i in range(0, len(line)-1, 2):
        size, space = int(line[i]), int(line[i+1])
        file = (size, space)
        files.append(file)
    if len(line) % 2 == 1:
        size, space = int(line[-1]), 0
        file = (size, space)
        files.append(file)
    return files


def get_memory_layout(files):
    memory_layout = []
    for id, (size, space) in enumerate(files):
        memory_layout.extend([id]*size)
        memory_layout.extend(['.']*space)
    return memory_layout


def advance(i, memory):
    while memory[i] != '.':
        i += 1
    return i


def decrease(j, memory):
    while memory[j] == '.':
        j -= 1
    return j


def move_file_blocks(memory):
    i = 0
    i = advance(i, memory)

    j = len(memory)-1
    j = decrease(j, memory)

    while i < j:
        memory[i], memory[j] = memory[j], memory[i]
        i = advance(i, memory)
        j = decrease(j, memory)

    return memory


if __name__ == '__main__':
    files = get_files()
    memory_layout = get_memory_layout(files)
    compacted_memory = move_file_blocks(memory_layout)

    sum = 0
    for i, id in enumerate(compacted_memory):
        if id == '.':
            break
        sum += i*id

    print(sum)

