a = eval(input()) or 'q'
dic = {}
while a != 'q':
    dic[a] = dic.get(a,0) + 1
    a = eval(input()) or 'q'
ls = list(dic.items())
ls.sort(key= lambda x :x[1],reverse=True)
print(ls[0][0],ls[0][1])


