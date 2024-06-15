A = eval(input())
for i in A:
    if i == 0:
        A.remove(i)
        A.append(i)
print(A)
