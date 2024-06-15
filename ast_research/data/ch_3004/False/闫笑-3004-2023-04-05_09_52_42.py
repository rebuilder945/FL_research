def sushu(n):
    for x in range(2,n//2+1):
        if n % x ==0:
            return False
        else:
            return True
a = eval(input())
b = []
for i in a:
    if i >= 2 and sushu(i):
        b.append(i)
print(b)
