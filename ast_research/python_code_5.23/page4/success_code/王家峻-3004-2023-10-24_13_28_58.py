n=eval(input())
for i in n:
    b=n[i]
    c=[]
    c.append(b)
    for x in range(2,b//2):
        if b % x==0:
            c.remove(b)
            print(c)
