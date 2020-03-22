import pronounce


def text_words2dict(filename):
    words_dict = dict()
    fin = open(filename)
    for line in fin.read().split('\n'):
        words_dict[line] = 1
    return words_dict


def invert_dict(the_dict):
    neo_dict = {}
    for key in the_dict:
        neo_dict.setdefault(the_dict[key], key)
    return neo_dict


known_ack = {}


def ack_plus(m, n):
    if (m, n) in known_ack:
        return known_ack[m, n]
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack_plus(m - 1, 1)
    else:
        return ack_plus(m - 1, ack_plus(m, n - 1))


def has_duplicates_plus(test_list):
    the_dict = {}
    for k in test_list:
        the_dict[k] = the_dict.get(k, 0) + 1
    for kk in the_dict:
        if the_dict[kk] < 2:
            return False
    return True


def rotate_string(the_string, rotate_delta):
    neo_string_list = []
    for c in the_string:
        neo_string_list.append(chr(ord('a') + (ord(c) - ord('a') + rotate_delta) % 26))
    return ''.join(neo_string_list)


def get_all_rotated_string(the_str):
    for i in range(26):
        print(rotate_string(the_str, i))


def find_homophone_word():
    pronounce_dict = pronounce.read_dictionary()
    result_list = []
    for test_word in pronounce_dict:
        if len(test_word) == 5:
            if test_word[1:] in pronounce_dict and (test_word[0] + test_word[2:]) in pronounce_dict:
                if pronounce_dict[test_word] == pronounce_dict[test_word[1:]] == \
                        pronounce_dict[test_word[0] + test_word[2:]]:
                    result_list.append(test_word)
            else:
                continue
    return result_list


# text_name = 'sample.txt'
# test_dict = {'aa': 123, 'bb': 3546, 'cc': 9.24}
print(','.join(find_homophone_word()))  # scent
