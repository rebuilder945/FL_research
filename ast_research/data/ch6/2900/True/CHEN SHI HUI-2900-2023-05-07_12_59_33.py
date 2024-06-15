def ss(a):
    if n>=2 and type(n)==int:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True
    else:
        return False
def hw(a):
    if str(a)==str(a)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n<2 or type(n)!=type(1):
    print('illegal input')
else:
    for i in range(2,n+1):
        if ss(i) and hw(i):
            print(i,end=' ')




