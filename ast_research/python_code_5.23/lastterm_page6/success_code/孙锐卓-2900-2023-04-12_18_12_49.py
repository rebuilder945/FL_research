def hui(x):
    h=str(x)
    if h==h[::-1]:
        return True
    else:
        return False
def su(x):
    b=0
    for i in range(2,x):
        if int(x/i)==x/i and b!=1:
            b=1
        elif b==1:
            break
    if b==1:
        return(False)
    else:
        return(True)
num=eval(input())
i=2
x=1
t=1
result=list()
n=list()
while x<=num:
    if hui(i) and su(i):
        result.append(i)
        i+=1
        x+=1
    else:
        i+=1
c=0
for i in result:
    print('{:6}'.format(i),end='')
    c+=1
    if c==10:
        print(end="\n")
        c=0












