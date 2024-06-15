def sushu(n):
    c = [0]
    for i in range(3,n):
        if n % i == 0:
            c.append(1)
    if sum(c) == 0:
        return True
    else:
        return False

a = eval(input())
b = []
for i in a:
    if sushu(i):
        b.append(i)
    else:
        continue
print(b)



