




def su(n):
    if n>=2:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False
def hui(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=input()
if type(n)!=type(1) or n<2:
    print("illegal input")
else:
    for i in range(2,n):
        if su(i) and hui(i):
            print(i,end='')

