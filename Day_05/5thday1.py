import math


def mysqrt(a):
    x = a / 2
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y


def print_blank_line(strings, blank_len):
    print(strings[0].ljust(blank_len[0], ' '), end=' ')
    print(strings[1].ljust(blank_len[1], ' '), end=' ')
    print(strings[2].ljust(blank_len[2], ' '), end=' ')
    print(strings[3].ljust(blank_len[3], ' '), end=' ')
    print()


def test_square_root(upnum):
    blank_len = [6, 20, 20, 20]
    print_blank_line(['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'], blank_len)
    print_blank_line(['-' * len('a'), '-' * len('mysqrt(a)'), '-' * len('math.sqrt(a)'), '-' * len('diff')], blank_len)

    for i in range(1, upnum + 1):
        i = float(i)
        print_blank_line(list(map(str, [i, mysqrt(i), math.sqrt(i), math.sqrt(i) - mysqrt(i)])), blank_len)


test_square_root(10)
