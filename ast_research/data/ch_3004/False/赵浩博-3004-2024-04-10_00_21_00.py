def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
a=eval(input())
a1=[]
for x in range(len(a)):
    if bool(sushu(a[x]))==True:
        a1.append(a[x])
if a1!=[]:    
    print(a1,end='')
else:
    print()
