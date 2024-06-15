a=(input())
c=[]
for i in a:
    a=a.count(i)
    if a==1:
        c.append(i)
    elif len(a)>=1:
        print(c[0])
    elif len(a)==0:
        print("None")
