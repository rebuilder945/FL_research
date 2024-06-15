def su(n):
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            return False
    else:
        return True
def hui(n):
    if str(n) == str(n)[::-1]:
        return False
    else:
        return True
n = eval(input())
if type(n) == float or n <2:
    print("illegal input")
else:
    for i in range(2,n):
        if su(n) and hui(n):
            print(i,end=' ')

