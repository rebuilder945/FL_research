ls1=eval(input())
ls2=[]
def sushu(n):
    for i in range(2,int(n*0.5)+1):
        if n % i == 0:
            return False
    return True
for j in ls1:
    if sushu(j):
        ls2.append(j)
print(ls2)
