def eval_loop(end_string):
    while True:
        get_string = input('>>>')
        if get_string != end_string:
            last_answer = eval(get_string)
            print(last_answer)
        else:
            break
    print(last_answer)


eval_loop('done')
