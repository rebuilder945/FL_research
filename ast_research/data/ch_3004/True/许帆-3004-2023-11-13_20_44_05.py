a = eval(input())
lst=[]
def sushu(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True

for i in a:
    if sushu(i) and i>1:
        lst.append(i)
print(lst)

