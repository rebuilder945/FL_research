def sushu(n):
    if n>=2:
        for x in range(2,n):
            if n%x==0:
                return False
            else:
                return True
    else:
        return False
a=eval(input())
b=[]
for x in range(0,len(a)):
    if sushu(x):
        b.append(x)
print(b)
        
