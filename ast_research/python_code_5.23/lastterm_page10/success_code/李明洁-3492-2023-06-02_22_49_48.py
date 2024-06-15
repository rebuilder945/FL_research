def first_not_repeating_char(strings):

    chars = []
    times = []
    if not strings:
        return None
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
    return False

strings = input('请输入长字符串：')
print('结果：', first_not_repeating_char(strings))
