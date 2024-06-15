a=eval(input())
b=3
s=[2]
while len(s)<a:
    if str(b)!=str(b)[::-1]:
        pass
    else:
        k=2
        while k<=b:
            if b%k==0:
                break
            else:
                k=k+1
        if k==b:
            s.append(b)
    b=b+1
n=0
while 10*n+9<=a-1:
    for x in range(10*n,10*n+9):
        print('{:6}'.format(s[x]),end="")
    print('{:6}'.format(s[10*n+9]))
    n=n+1
for x in range(10*n,a):
    print('{:6}'.format(s[x]),end="")


