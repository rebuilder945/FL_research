def prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def palindprome(num):
    return str(num)==str(num)[::-1]
n=eval(input())
if n<=0 or type(n)==float:
    print("illegal input")
else:
    for x in range(n):
        if prime(x) and palindprome(x):
            print(format(x,"1d"),end=" ")
        else:
            pass


