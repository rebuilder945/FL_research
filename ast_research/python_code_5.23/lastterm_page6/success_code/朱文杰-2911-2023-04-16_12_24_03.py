n=list(input())
m=[]
for x in n:
    x=(int(x)+5)%10
    m.append(x)
m=m[::-1]
for x in m:
    print(x,end="")
