a = eval(input())
b = []
if a == 1:
    print([1])
if a == 2:
    print([2,1])
if a > 2:
    for i in range(2,a+1):
        b.append(i)
b.append(1)
print(b)
