def first_not_repeating_char(strings):
    '''
        查找给定字符串中第一个次数为1的字符
    :param strings: str，查找字符串
    :return: str，第一个次数为1的字符
    '''
    chars = []
    times = []
    for s in strings:
        if s not in chars:
            chars.append(s)
            times.append(1)
        else:
            char_index = chars.index(s)
            times[char_index] += 1

    for t in times:
        if t == 1:
            times_index = times.index(t)
            return chars[times_index]
    return None

strings = input()
print(first_not_repeating_char(strings))

