lst=eval(input())
def sushu(x):
    if x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True

lst2=[]
for x in lst:
    if sushu(x):
        lst2.append(x)
print(lst2)
