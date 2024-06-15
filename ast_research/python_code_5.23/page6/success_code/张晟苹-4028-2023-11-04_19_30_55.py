def huiwen(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
def sushu(i):
    if i>=2 and type(i)==int:
        for x in range(2,i//2+1):
            if i%x==0:
                return False
    return True
a=eval(input())
if a>1 and type(a)==int:
    for y in range(a):
        if huiwen(y) and sushu(y) and y>1:
            print(y,end=' ')
else:
    print('illegal input')





