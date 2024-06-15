def su(x):
    if x<2:
        return False
    for i in range (2,x):
        if x% i ==0:
            return False
        
    return True

def hui(x):
    p=x
    k=0
    while p!=0:
        k=k*10+p%10
        p=p//10
    if k==x:
        return True
    else:
        return False

m=eval(input())
if m<=1 or type(m)==float:
    print('illegal input')
else:
    for i in range(0,m+1):
        if su(i)==True and hui(i)==True: 
            print(i,end=' ')

