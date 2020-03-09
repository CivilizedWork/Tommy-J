def draw_a_line(column):
    print('+', end='')
    for j in range(column):
        print('----+', end='')
    print()


def test1(raw, column):
    draw_a_line(column)
    for i in range(raw):
        for k in range(4):
            print('|', end='')
            for j in range(column):
                print('    |', end='')
            print()
        draw_a_line(column)


test1(4,4)
