a = eval(input())
a.sort(reverse = True)
c = []
for x in a:
    if len(a)==3 and a[0]==0:
        print("0",end="")
    else: 
        c.insert(0,x)
        print(c[0],end="")

