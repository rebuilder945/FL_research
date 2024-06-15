a=(input())
c=[]
for i in a:
    b=a.count(i)
    if b==1:
        c.append(i)
    elif len(c)>=1:
        print(c[0])
    elif len(c)==0:
        print("None")
