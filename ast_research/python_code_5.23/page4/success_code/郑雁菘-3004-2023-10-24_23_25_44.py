A = eval(input())
B = []
D = []
k = 0
for i in A:
    if i <= 1:
        D.append(i)
    else:
        for j in range(2,i):
            if i % j == 0:
               B.append(i)
               C = set(B)
M = list(C)
for m in C:
    A.remove(m)
for n in D:
    A.append(m)
print(A)



       


