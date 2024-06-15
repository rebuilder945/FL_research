ls1 = eval(input())
for i in ls1:
    if i == 0:
        ls1.remove(i)
        ls1.append(i)
print(ls1)
