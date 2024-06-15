a = input().split()
dic = {}
for x in a:
    if x not in dic:
        dic[x]=1
    else:
        dic[x]+=1
n = list(dic.items())
n.sort(key=lambda x:x[0])
n.sort(key=lambda x:x[1],reverse=True)
for y in n:
    if y[1] == n[0][1]:
        print(y[0],y[1])
    else:
        break
