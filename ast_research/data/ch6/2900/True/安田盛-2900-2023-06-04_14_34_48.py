def hui(a):
    if str(a)[::-1]==str(a):
        return True
def su(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    else:
        return True
    




n=eval(input())
if n<=1 or type(n)==float:
    print("illegal input")
else:
    for i in range(2,n):
        if hui(i) and su(i):
            print(i,end=" ")
    





