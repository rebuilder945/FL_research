p = input().split()
dic = {'name':p[0],'english':p[1],'python':p[2],'math':p[3]}
avg1 = 0
for x in dic:
    if x !='name':
        avg1 += dic[x]
avg = avg1/3
n = list(dic.items())[2:]
n.sort(key=lambda x:x[1],reverse=True)
print(dic['name'],end=' ')
for x in n:
    print(x[1],end=' ')
print(avg)
