def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True
a=eval(input())
if sushu(a):
    t=[b for b in range(len(a))]
    print(t)


