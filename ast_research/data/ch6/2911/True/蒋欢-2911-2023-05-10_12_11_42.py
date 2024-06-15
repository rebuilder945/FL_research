def jiami(n):
    a=[]
    for p in n:
        a.append(p)
    m=[]
    for x in a:
        x=int(x)
        m.append((x+5)%10)
    m.reverse()
    for i in m:
        print(i,end="")
n=input()
jiami(n)
