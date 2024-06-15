s=input()
a={}
for i in s:
    if i=='q':
        break
    else:
        a[i]=a.get(i,0)+1
a.sort(key=lambda x:x[1],reverse=True)
print(a[0])


