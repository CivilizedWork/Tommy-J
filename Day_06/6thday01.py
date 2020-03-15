def string_count(the_string, the_char):
    count = 0
    for i in the_string:
        if the_char == i:
            count += 1
    return count


def is_palindrome_upgraded(the_string):
    return the_string == the_string[::-1]


def rotate_word(the_string, the_num):
    neo_string = ''
    for i in the_string:
        neo_ord=ord(i)+the_num
        if (ord('A') < ord(i) < ord('Z') < neo_ord) or (
                ord('a') < ord(i) < ord('z') < neo_ord):
            neo_ord -= 26
        elif (ord('Z') > ord(i) > ord('A') > neo_ord) or (
                ord('z') > ord(i) > ord('a') > neo_ord):
            neo_ord+=26
        neo_string += chr(neo_ord)
    return neo_string


print(rotate_word('YAHAHA',2))
