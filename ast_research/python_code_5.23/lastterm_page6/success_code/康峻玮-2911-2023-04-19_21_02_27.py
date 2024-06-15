ls=list(input())
m=[]
for x in ls:
    y=x+5
    d=y%10
    m.append(d)
m=m[::-1]
for x in m:
    print(x,end="")



