def s(i):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def h(i):
    for i in range(2,n):
        if str(n)[::-1]==str(n):
            return True
        else:
            return False
        
n=eval(input())
if n>=1 and type(n)==type(2):
    for i in range(2,n):
        if s(i) and h(i):
            print(i,end='')
else:
    print('illegal input')
