lst=eval(input())
lst2=[]
def sushu(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for x in lst:
    if sushu(x):
        lst2.append(x)
print(lst2)

