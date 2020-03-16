def nested_sum(nested_list):
    sum = 0
    for lists in nested_list:
        for i in lists:
            sum += i
    return sum


def cumsum(the_list):
    cum_list = []
    for i in range(len(the_list)):
        sum_up = 0
        for j in range(i + 1):
            sum_up += the_list[j]
        cum_list.append(sum_up)
    return cum_list


def middle(origin_list):
    return origin_list[1:-1]


def chop(origin_list):
    del origin_list[0], origin_list[-1]


def is_sorted(tested_list):
    sorted_list = []
    sorted_list.extend(tested_list)
    sorted_list.sort()
    return tested_list == sorted_list


def is_anagram(*tested_2_string):
    tested_2_list = []
    for the_string in tested_2_string:
        string_2_list = list(the_string)
        string_2_list.sort()
        tested_2_list.append(string_2_list)
    return tested_2_list[0] == tested_2_list[1]


def is_duplicates(tested_string):
    char_list = []
    bool_list = []
    for i in tested_string:
        if i not in char_list:
            char_list.append(i)
            bool_list.append(False)
        else:
            bool_list[char_list.index(i)] = True
    for i in bool_list:
        if not i:
            return False
    return True


def same_birthday(student_num):
    from random import randint
    count = 0
    birthdays = []
    for i in range(student_num):
        one_day = randint(1, 365)
        count += 1
        if one_day in birthdays:
            return False
        else:
            birthdays.append(one_day)

    return True


def birthday_experiment(test_times, student_num):
    count = 0
    for i in range(test_times):
        if same_birthday(student_num):
            count += 1
    return count / test_times




