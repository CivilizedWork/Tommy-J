import time
import random


def time2_readabletime(time):
    second = int(time % 60)
    time /= 60
    minute = int(time % 60)
    time /= 60
    hour = int(time % 24)
    time /= 24
    print(int(time), hour, minute, second)


def fermat_check():
    [a, b, c, n] = map(int, input('input 4 numbers separated by commas:').split(','))
    if n <= 2:
        print('it can\'t tell anything.')
        return
    else:
        if a ** n + b ** n == c ** n:
            print ('Holy smokes, Fermat was wrong!')
        else:
            print('No, that doesn’t work.')


def is_triangle():
    triangle = list(map(int, input('input 3 numbers separated by commas:').split(',')))
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        print('Yes')
    else:
        print('No')


#resourse函数的作用为返回1到n的累加和，但其缺陷在于若输入负数或者浮点数时会陷入死循环，改进方法可将判断条件中的==0改为<=0

