def jiami(n):
    n=n.split()
    m=[]
    for x in n:
        x=int(x)
        m.append((x+5)%10)
    m.reverse
    for i in m:
        print(i,end="")
n=input()
jiami(n)    
