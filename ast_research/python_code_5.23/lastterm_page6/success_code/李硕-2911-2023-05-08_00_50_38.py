a=list(input())
b=[]
for x in a:
    t=(int(x)+5)%10
    b.append(t)
b=b[::-1]
for l in b:
    print(l,end="")

    




