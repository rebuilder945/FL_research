a = eval(input())
a.sort(reverse = True)
c = []
for x in a:
    if len(a)==0 and a[0]==0:
        print("0")
    else: 
        c.insert(0,x)
        print(c[0],end="")

