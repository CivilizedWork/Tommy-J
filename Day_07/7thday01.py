def print_more_than_20(filename):
    fin = open(filename)
    for line in fin:
        if len(line) > 20:
            print(line)


def has_no_e(tested_string):
    for i in tested_string:
        if i == 'e':
            return False
    return True


def exercise_2(filename):
    fin = open(filename)
    line_num = 0
    line_no_e_num = 0
    for line in fin:
        line_num += 1
        if has_no_e(line):
            line_no_e_num += 1
            print(line)
    print(line_no_e_num / line_num)


def avoids(tested_word, forbidden_letters):
    for forbidden_char in forbidden_letters:
        for i in tested_word:
            if i == forbidden_char:
                return False
    return True


def uses_only(tested_word, only_letters):
    for i in tested_word:
        count = 0
        for only_char in only_letters:
            count += 1
            if only_char == i:
                break
            if count == len(only_letters):
                return False
    return True


def uses_all(tested_word, all_letters):
    for all_char in all_letters:
        if all_char not in tested_word:
            return False
    return True


def is_abecedarian(the_string):
    last_char = the_string[0]
    for i in the_string:
        if not (i == last_char or ord(i) == ord(last_char) + 1):
            return False
        last_char = i
    return True


# exercise_2('Sample.txt')
# print(uses_all('bananta', 'bnwa'))
print(is_abecedarian('abbcdewefg'))
