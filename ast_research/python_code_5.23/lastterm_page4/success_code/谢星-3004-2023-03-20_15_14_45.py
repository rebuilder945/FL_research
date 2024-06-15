def sushu(n):
    if n==0 or n==1:
        return False
    count=0
    for i in range(2,n):
        if n%i==0:
            count=count+1
            if count!=0:
                return False
    else:
        return True
    
a=eval(input())
b=[]
for i in a:
    if sushu(i):
        b.append(i)
print(b)



