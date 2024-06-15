a = eval(input())
lst=[]
def sushu(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True
if 2 in a:
    lst.append(2)
for i in a:
    if sushu(i):
        lst.append(i)
print(lst)

