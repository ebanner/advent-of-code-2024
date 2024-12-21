output = [2, 4, 1, 5, 7, 5, 4, 5, 0, 3, 1, 6, 5, 5, 3, 0]


def f(a1):
    b1 = a1 % 8
    b2 = b1 ^ 5
    c = a1 >> b2
    b3 = b2 ^ c
    a2 = a1 >> 3
    b4 = b3 ^ 6
    out = b4 % 8
    return out


def search(string_that_works_so_far, output_idx):
    def get_test_string(string_that_works_so_far, i):
        candidate_string = bin(i)[2:].zfill(3)
        test_string = string_that_works_so_far + candidate_string
        return test_string

    if output_idx == -1:
        return int(string_that_works_so_far, 2)

    min_a = float('inf')
    for i in range(8):
        test_string = get_test_string(string_that_works_so_far, i)
        a1 = int(test_string, 2)
        out = f(a1)
        if out == output[output_idx]:
            a = search(test_string, output_idx-1)
            min_a = min(a, min_a)

    return min_a


if __name__ == '__main__':
    min_a = search('', 15)
    print(min_a)
