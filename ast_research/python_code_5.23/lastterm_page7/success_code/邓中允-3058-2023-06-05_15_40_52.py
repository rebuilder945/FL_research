s=list(input().split(' '))
a={}
for i in s:
    if i=='q':
        break
    else:
        a[i]=a.get(i,0)+1
b=[]
for k,v in a.items():
    b.append([k,v])
b.sort(key=lambda x:x[1],reverse=True)
print(b[0])


