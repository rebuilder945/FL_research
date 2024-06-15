def susu(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def huiwen(x):
    x=str(x)
    b=1
    for i in range(len(x)):
        if x[i]==x[-1-i]:
            b=1
        else:
            b=2
            break
    if b==1:
        return True
    return False
x=eval(input())
b=[]
c=[]
if  x!=float and x>1:
    for i in range(2,x):
        if susu(i) is True:
            b.append(i)
    for i in b:
        if huiwen(i) is True:
            c.append(i)
    print(' '.join(map(str,c)))
else:
    print('illegal input')


