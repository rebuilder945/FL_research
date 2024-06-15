def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
a= eval(input())
ls=[]
for x in a:
    if sushu(x) and x!=1:
        ls.append(x)
print(ls)

