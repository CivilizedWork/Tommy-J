def most_frequent(the_string):
    new_dict = {}
    for c in the_string:
        new_dict[c] = new_dict.get(c, 0) + 1
    fre_list = []
    for letter, frequency in new_dict.items():
        fre_list.append((frequency, letter))
    fre_list.sort(reverse=True)
    for frequency, letter in fre_list:
        print('%s\t%d' % (letter, frequency))



