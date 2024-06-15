a = ''
dic = {}
while a != 'q':
    a = input()
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1
n = list(dic.item())
n.sort(key=lambda x:x[1],reverse=True)
print(n[0][0],n[0][1])
