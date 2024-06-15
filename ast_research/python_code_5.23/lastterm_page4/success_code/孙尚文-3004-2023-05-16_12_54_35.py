def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True
a=input()
b=[]
for i in a:
    if sushu(i):
        b.append(i)
print(b)

