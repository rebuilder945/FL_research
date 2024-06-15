str=input().split
a={}
for i in str:
    if i not in a:
        a[i]=1
    else:
        a[i]+=1
print(a)
