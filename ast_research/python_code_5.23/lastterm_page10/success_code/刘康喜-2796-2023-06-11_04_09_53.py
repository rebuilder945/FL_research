a=input()
b=['1','2','3','4','5','6','7','8','9','0']
m=[1,2,3,4,5,6,7,8,9,0]
l=[]
r=[]
e=[]
for i in range(0,len(a)):
    if i==0:
        if a[i] in b:
            l.append(i)
    elif i ==len(a)-1:
        if a[i] in b:
            r.append(i)
    elif a[i] in b and a[i-1] not in b:
        l.append(i)
    elif a[i] not in b and a[i-1] in b:
        r.append(i)
if len(l)==0:
    print('No digits')
else:
    for i in range(0,len(r)):
        d=r[i]-l[i]
        e.append(d)
    c=max(e)

    for j in range(0,len(e)):
        if e[j]==c:
            x=j
        g=a[l[x]:r[x]]
    print(g)




