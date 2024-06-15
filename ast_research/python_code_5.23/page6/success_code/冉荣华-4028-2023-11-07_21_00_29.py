def s(n):
    if n >=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%1==0:
                return False
        return True
    else:
        return False
def h(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n<2 or type(n)!=int:
    print("illegal input")
else:
    for i in range(2,n):
        if s(i) and h(i):
            print(i,end='')



