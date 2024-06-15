n1 = eval(input())
m1 = min(n1)
m2 = max(n1)
n2 = []
for i in n1:
    if i != m1 and i != m2:
        n2.append(i)
print(n2)
