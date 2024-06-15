a = input().split()
dic = {}
for i in a:
    dic[i] = dic.get(i,0) + 1
ls = list(dic.items())
ls.sort(key=lambda x :x[1],reverse= True)
b = ls[0][1]
for i in ls:
    if i[1] == b:
        print(i[0],i[1])
    else:
        break


