A = eval(input())
B = A.copy()
m = max(A)
n = min(A)
for i in B:
    if i == m or i == n:
        A.remove(i)
print(A)


