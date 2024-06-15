s = input()
dic = {}
while s != 'q':
    dic[s] = dic.get(s,0) + 1
    s = input()
lst = list(dic.items())
lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][0],lst[0][1])
