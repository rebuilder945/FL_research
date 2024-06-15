Ls=list(eval(input()))
n,m=eval(input())
r=len(Ls)
if abs(int(n)) < r and int(n) > 0:
    a = 0
    while a < int(m):
        Ls.append(Ls[int(n)])
        a = a+1
    print(Ls)
elif abs(int(n)) < r and int(n) <0:
    b = 0    
    while b < int(m):
        Ls.append(Ls[int(n)+r])
        b = b+1
    print(Ls)
else:
    print("error")
