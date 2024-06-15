a=list(input())
m=[]
for x in a:
    x=(int(x)+5)%10
    m.append(x)
m.reverse()
for x in m:
    print(x,end=(""))

