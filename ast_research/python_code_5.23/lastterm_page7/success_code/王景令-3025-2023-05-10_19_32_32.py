a = input().split()
dic = {}
for i in a:
    dic[i] = dic.get(i,0) + 1
ls = list(dic.items())
ls.sort(key=lambda x :x[1],reverse= True)
b = ls[0][1]
ls2 = []
for i in ls:
    if i[1] == b:
        ls2.append(i)
    else:
        break
ls2.sort(key= lambda x : x[0])
for i in ls2:
    print(i[0],i[1])

