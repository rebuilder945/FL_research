s = input()
dic = {}
while s != 'q':
    dic[s] = dic.setdefault(s,0) + 1
    s = input() or 'q'
e = max(dic,key = lambda x: dic[x])
print(e,dic[e])

