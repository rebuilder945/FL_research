b = []
a = eval(input())
while type(a) is int:
    b.append(a)
    a = eval(input())
print(len(b),end=" ")
print(sum(b))

