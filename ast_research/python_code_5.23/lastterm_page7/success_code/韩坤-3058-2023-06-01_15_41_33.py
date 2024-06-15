a={}
while True:
    x=input()
    if x=='q':
        break
    a[x]=a.get(x,0)+1
a=list(a.items())
a.sort(key=lambda x:x[1],reverse=True)
print(a[0][0],a[0][1])
