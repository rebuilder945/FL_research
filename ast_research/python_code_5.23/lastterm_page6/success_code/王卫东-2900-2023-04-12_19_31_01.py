def ss(a):
    for x in range(2,n//2+1):
        if a%x==0:
            return False
    return True
def hw(a):
    if str(a)==str(a)[::-1]:
        return True
    else:
        return False
n=int(input())
if type(n)!=type(1) or n<2:
    print("illegal input")  
else:
    for y in range(2,n):
        if ss(y) and hw(y):
            print(y,end=' ')            

