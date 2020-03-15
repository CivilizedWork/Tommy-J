def is_3_consecutive_double_letter_word(tested_word):
    last_char = ''
    repeated = True
    count = 0
    max_count = 0
    for i in tested_word:
        if (i == last_char) == repeated:
            if repeated:
                count += 1
            repeated = not repeated
        else:
            if count > max_count:
                max_count = count
            if not repeated:
                count = 1
            else:
                count = 0
        last_char = i
    return max_count


def is_palindrome_upgraded(the_string):
    return the_string == the_string[::-1]


def find_odometer():
    for i in range(100000, 1000000):
        if is_palindrome_upgraded(str(i)[2:]):
            if is_palindrome_upgraded(str(i + 1)[1:]):
                if is_palindrome_upgraded(str(i + 2)[1:5]):
                    if is_palindrome_upgraded(str(i + 3)):
                        return i
    return -1


# print(is_3_consecutive_double_letter_word('aaabbcccwccd'))
print(find_odometer())
