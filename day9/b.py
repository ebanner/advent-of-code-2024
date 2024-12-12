import sys

from tqdm import tqdm


def get_files():
    line = sys.stdin.readline().strip()
    files = []
    id = 0
    for i in range(0, len(line)-1, 2):
        size, space = int(line[i]), int(line[i+1])
        file = [id, size, space]
        files.append(file)
        id += 1
    if len(line) % 2 == 1:
        size, space = int(line[-1]), 0
        file = [id, size, space]
        files.append(file)
    return files


def get_memory_layout(files):
    memory_layout = []
    for id, size, space in files:
        memory_layout.extend([id]*size)
        memory_layout.extend(['.']*space)
    return memory_layout


def find(id, memory):
    for i in range(len(memory)):
        if memory[i] == id:
            return i


def compact_files(memory, files):
    for id, size, _ in tqdm(list(reversed(files))):
        i = find(id, memory)
        for j in range(len(memory)):
            if j == i:
                break
            if memory[j:j+size] == ['.']*size:
                memory[j:j+size] = memory[i:i+size]
                memory[i:i+size] = ['.']*size
    return memory


if __name__ == '__main__':
    files = get_files()
    memory = get_memory_layout(files)
    compacted_memory = compact_files(memory, files)

    sum = 0
    for i, id in enumerate(compacted_memory):
        if id == '.':
            continue
        sum += i*id

    print(sum)

