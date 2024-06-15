def su(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    else:
        return True
def hui(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = eval(input())
if type(n) == float or n <2:
    print("illegal input")
else:
    for i in range(2,n):
        if su(n) and hui(n):
            print(i,end=' ')

