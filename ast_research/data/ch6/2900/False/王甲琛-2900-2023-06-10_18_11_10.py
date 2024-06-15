def sushu(n):
    if n>=2:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False     
def huiwen(n):
    n=str(n)
    lst1=[]
    for i in n:
        lst1.append(i)
    lst1.reverse()
    str1="".join(lst1)
    if str1==n:
        return True
    else:
        return False
def huisu(n):
    if sushu(n) and huiwen(n):
        return True
    else:
        return False
n=eval(input())
if type(n)==int :
    for i in range(n):
        if huisu(i):
            print(i,end=" ")
else:
    print('illegal input')
