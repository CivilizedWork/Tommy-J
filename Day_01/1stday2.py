#无法以42=a的形式赋值；
#x=y=1的赋值是合法的，相当于连续赋值；
#python中分号的作用同C语言，结束一句代码，在句末是否用分号并没有实际影响；
#（英文）句号在python中被当作你小数点处理
#xy这种写法会被当作新的变量处理


def test1():
    pi = 3.1415926535897932
    radiu = int(input("Input radiu:"))
    volume = 4/3*pi*radiu**3
    print(volume)


def test2():
    price=24.95
    book_amount=60
    discont=0.60
    wholesale_cost=price*discont*book_amount+((book_amount-1)*0.75+3)
    print(wholesale_cost)


def minute2second(minute, second):
    return minute * 60 + second


def test3():
    easy_pace = 1/minute2second(8, 15)
    tempo = 1/minute2second(7, 12)
    totletime=(1/easy_pace+3/tempo+1/easy_pace)/60
    print(totletime)


test3()
