dic = {}
while True:
    stri = input()
    if stri in dic:
        dic[stri] += 1
    if stri not in dic:
        dic[stri] = 1
    if stri == 'q':
        break
lst1 = list(dic.values())
lst2 = list(dic.keys())
imax = max(lst1)
a = lst1.index(imax)
print('{} {}'.format(lst2[a], imax))
