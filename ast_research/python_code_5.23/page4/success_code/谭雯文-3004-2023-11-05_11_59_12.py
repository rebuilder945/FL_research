def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return n
a=eval(input())
b=[]
for i in a:
    if i==sushu(i):
        b.append(i)
        
print(b)
    



