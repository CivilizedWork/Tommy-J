def test1():
    minute = int(input("Input minutes:"))
    second = int(input("Input seconds:"))
    print('There R {:d} seconds.'.format(minute * 60 + second))


def test2():
    kilometre = int(input("Input kilometres:"))
    print('There R {:.4f} kilometres.'.format(kilometre / 1.61))


def test3():
    minute = int(input("Input minutes:"))
    second = int(input("Input seconds:"))
    kilometre = int(input("Input kilometres:"))

    total_second = minute * 60 + second
    mile = kilometre / 1.61

    print("The average pace is {:.4f}.\nThe average speed per hour is {:.4f}.".format\
              (mile/total_second, kilometre/(total_second/3600)))

test3()