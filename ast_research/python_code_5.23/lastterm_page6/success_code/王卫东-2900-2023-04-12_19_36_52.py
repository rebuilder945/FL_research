def ss(n):
    for x in range(2,n):
        if n%x==0:
            return False
    return True
def hw(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n =int(input())
if n<2 or type(n)!=type(1):
    print("illegal input")  
else:
    for x in range(2,n+1):
        if ss(x) and hw(x):
            print(x,end=' ')            

