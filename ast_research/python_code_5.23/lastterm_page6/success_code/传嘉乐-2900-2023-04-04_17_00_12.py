def s(n):
    if n>=2 and type(n)==type(2):
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False
def h(n):
    if str(n)[::-1]==str(n):
        return True
    else:
        return False
    
n=eval(input())
if n<2 and type(n)!=type(2):
    print('illegal input')
else:
    for i in range(2,n):
        if s(n) and h(n):
            print(i,end='')
    
