def sushu(n):
    ls1=[]
    ls2=[]
    for x in range(2,n+1):
        ls1.append(x)
        for i in range(2,x):
            if x%i==0:
                ls2.append(x)
            else:
                continue
    ls3=ls1.copy()
    ls4=[]
    for x in ls3:
        if x not in ls2:
            ls4.append(x)
            
    return ls4
def huiwenshu(n):
    ls2=[]
    for x in range(2,n+1):
        y=str(x)[::-1]
        if int(y)==x:
            ls2.append(x)
    return ls2
n=input()
if int(float(n))<0 or float(n)!=int(float(n)):
    print('illegal input')
else:
    n=int(float(n))
    ls1=sushu(n)
    ls2=huiwenshu(n)
    ls3=ls1.copy()
    ls4=[]
    for x in ls3:
        if x in ls2:
            ls4.append(x)
        else:
            continue
    ls4.sort()
    for i in ls4:
        print(i,end=' ')


        
    




