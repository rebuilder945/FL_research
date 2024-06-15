def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0 or n<2:
            return False
    return True
a=eval(input())
a1=[]
for x in a:
    if bool(sushu(x))==True:
        a1.append(x)
if a1!=[]:    
    print(a1,end='')

