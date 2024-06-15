A = eval(input())
B = set(A)
for i in A:
    m = max(B)
    if i == m:
        A.remove(i)
for i in A:
    n = min(B)
    if i == n:
        A.remove(i)
print(A)




