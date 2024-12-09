import sys


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


def insert(j, i, files):
    new_files = files[:i+1] + files[j:j+1] + files[i+1:]
    return new_files


def remove(j, files):
    new_files = files[:j] + files[j+1:]
    return new_files


def find(source_id, files):
    for j, (id, _, _) in enumerate(files):
        if id == source_id:
            return j


def move(j, i, files):
    files = insert(j, i, files)
    files = remove(j+1, files)
    return files


def compact_files(files):
    j = len(files)-1
    SPACE_IDX = 2
    for source_id, source_size, source_free_space in reversed(files):
        j = find(source_id, files)
        for i, (_, _, free_space) in enumerate(files):
            if i == j:
                break
            if free_space >= source_size:
                files[j-1][SPACE_IDX] += source_size + source_free_space
                files[j][SPACE_IDX] = free_space - source_size
                files[i][SPACE_IDX] = 0
                files = move(j, i, files)
                break
    return files


if __name__ == '__main__':
    files = get_files()
    compacted_files = compact_files(files)
    memory = get_memory_layout(compacted_files)

    sum = 0
    for i, id in enumerate(memory):
        if id == '.':
            continue
        sum += i*id

    print(sum)

