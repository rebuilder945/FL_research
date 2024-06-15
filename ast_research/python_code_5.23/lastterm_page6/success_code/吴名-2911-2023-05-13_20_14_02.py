n=list(input())
m=[]
for i in n:
    a=(eval(i)+5)%10
    m.insert(0,a)
for i in m:
    print(i,end='')
