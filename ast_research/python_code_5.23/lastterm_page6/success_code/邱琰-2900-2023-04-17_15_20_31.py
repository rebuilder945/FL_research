def huiwen(n):
    s=str(n)
    if s==s[::-1]:
        return True
    else:
        return False
def sushu(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=eval(input())
if n<=0 or type(n)==float:
    print('illegal input')
else:
    lst=[]
    for i in range(2,n):
        if huiwen(i) and sushu(i):
            lst.append(i)
print(lst)
