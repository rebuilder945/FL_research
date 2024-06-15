lst = input().split()
dic = {}
for i in lst:
    dic[i] = lst.count(i)
imax = max(list(dic.values()))
for i in dic.keys():
    if dic[i] == imax:
        print('{} {}'.format(i, imax))
