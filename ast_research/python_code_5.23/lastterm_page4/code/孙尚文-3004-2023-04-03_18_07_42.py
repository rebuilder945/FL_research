def sushu(n):
    if n==0 or n==1:
        return False
    else:
        for x in range(0,n-1)
            if x%n==0:
                return True
            else:
                return False
a=eval(input())
b=[]
for x in range(0,len(a)):
    b.append(sushu(a))
print(b)
        
