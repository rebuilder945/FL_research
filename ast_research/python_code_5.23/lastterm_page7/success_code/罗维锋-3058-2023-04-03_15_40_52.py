flag=''
a={}
while flag!="q":
    s=input()
    if s not in a.keys:
        a[s]=1
    else:
        a[s]+=1
    flag=s
m=a.values.index(max(a.values))
print(a.keys[m])






