def sushu(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=eval(input())
r=[]
for n in num:
    r.append(n)
print(r)



