n=input().split()
dic={}
for i in n:
    dic[i]=dic.get(i,0)+1
a=list(dic.items())
a.sort(key=lambda x:x[1])
b=[]
for x in range(len(a)-1):
    while a[x][1]==a[x+1][1]:
        b.append(a[x])
        break
b.append(a[-1])
b.sort(key=lambda x:x[0])
for k,v in b:
    print(k,v)


