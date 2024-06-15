a=eval(input())
b=a.copy()
c=[]
for i in b:
    if i.count<=1:
        c.append(i)
        print(c[0])
    else:
        print("None")
