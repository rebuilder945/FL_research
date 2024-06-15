def su(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True
n=eval(input())
if n<0 or int(n)<n:
    print("illegal input")
else:
    for i in range(1,n+1):
        if su(i):
            if str(i)==str(i)[::-1]:
                print(i)

