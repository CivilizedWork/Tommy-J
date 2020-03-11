def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


# middle函数（列表索引为1：-1时）的输出值为：若字符长度为0到2时，输出空字符串，否则输出从第一个与最后一个之间所有字符的字符串

def is_palindrome(the_string):
    if the_string[0] != the_string[-1]:
        return False
    elif len(the_string) > 2:
        return is_palindrome(the_string[1:-1])
    else:
        return True


print(is_palindrome('asdffdsa'))
