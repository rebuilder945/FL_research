def ss(n):
    for x in range(2,n//2+1):
        if n%x==0:
            return False
    return True
def hw(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
a=[2]
if type(n)==int and n>1:
    for x in range(3,n):
        if ss(x) and hw(x):
            a.append(x)
    print(" ".join(map(str,a)))        
else:
    print("illegal input")

