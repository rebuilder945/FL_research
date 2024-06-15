def isP(n):
    for k in range(2,n//2+1):
        if n%k==0:
            return False
    return True
a=[]
for i in range(2,1000):
    if isP(i) and isP(int(str(i)[::-1])) and i==int(str(i)[::-1]):
        a.append(i)
    print(*a)
