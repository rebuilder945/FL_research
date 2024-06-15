s = input()
lst = [*s]
lst2 = []
dct = {}
if s.isalpha():
    print('No digits')
else:
    for i in range(len(s)):
        for x in range(len(s)-i):
            if lst[i].isdigit() and lst[i+x].isdigit():
                if s[i:i+x].isdigit():
                    dct[s[i:i+x+1]] = len(s[i:i+x+1])
    for key in dct:
        if dct[key] == max(list(dct.values())):
            lst2.append(key)
    print(lst2[-1])

#注意index！！！注意index！！！注意index！！！呜呜~

