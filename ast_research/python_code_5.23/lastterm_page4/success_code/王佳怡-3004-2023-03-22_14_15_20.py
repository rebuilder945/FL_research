l=eval(input())
l1=list(l)
l2=[]
def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
for x in l1:
    if sushu(x):
        l2.append(x)
print(l2)
