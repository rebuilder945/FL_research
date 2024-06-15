n=input().split()
a=int(n[0])
b=int(n[1])
if 0<=a and b<=9 and b-a>=3:
    for x in range(a,b):
        s=""
        s=s+str(x)
        c=s
        for y in range(a,b):
            s=c
            s=s+str(y)
            d=s
            for z in range(a,b):
                s=d
                s=s+str(z)
                if s[0]!=s[1] and s[0]!=s[2] and s[1]!=s[2] and s[0]!="0":
                    print(s,end=' ')
else:
    print("illegal input")
