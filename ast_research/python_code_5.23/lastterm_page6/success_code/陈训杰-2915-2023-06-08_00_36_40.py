def isshui(n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**3
    if s==int(n):
        return 1
    return 0
n= eval(input())
m=[]
for i in range(2,n+1):
    if isshui(i):
        print(i)
        m.append(i)
if len(m)==0:
    print("none")
