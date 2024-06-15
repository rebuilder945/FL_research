def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
a=eval(input())
b=[]
for n in a:
    if n!=1 and n!=0 and sushu(n):
        b.append(n)
print(b)
