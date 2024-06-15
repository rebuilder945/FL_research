def first_char(str):
    dic = {}
    if i not in str:
        return None
    for i in range(len(str)):
        if str[i] in dic:
            dic[str[i]] += 1
        else:
            dic[str[i]] == 1
    for i in range(len(str)):
        if dic[str[i]] == 1:
            return str[i],i+1
if __name__=='__main__':
    str1 = input()
    print(first_char(str1))
