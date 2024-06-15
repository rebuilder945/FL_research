def sushu(n):
    if n==0 or n==1:
        return False
    else:
        for x in range(2,n):
            if n%x==0:
                return False
            else:
                return True
a=eval(input())
b=[]
for x in range(0,len(a)):
    if sushu(x):
        b.append(x)
print(b)
        
