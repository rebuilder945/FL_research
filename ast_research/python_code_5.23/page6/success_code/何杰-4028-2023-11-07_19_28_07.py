def shusu(n):
    if n>=2 and type(n)==int:
        for x in range(2,n//2+1):
            if n%x==0:
                return False 
        else:
            return True
    else:
        return False
def hws(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n<=0 or n-(n//1)!=0:
    print("illegal input")
else:
    for x in range(1,n+1):
        if shusu(x)and hws(x):
            print(x,end=' ')
