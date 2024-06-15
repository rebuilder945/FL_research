def first_char(str):
    dic = {}
    for i in range(len(str)):
        #累计字符的出现次数
        if str[i] in dic:
            dic[str[i]] += 1
        #只出现一次，key对应的value就记1次
        else:
            dic[str[i]] = 1
    for i in range(len(str)):
        if dic[str[i]] == 1:
            return str[i], i+1
if __name__ == '__main__':
    str1 = input()
    print(first_char(str1))

