n1 = eval(input())
n2 = []
n1.reverse()
for x in n1:
    if x not in n2:
        n2.append(x)
n2.reverse()
print(n2)
