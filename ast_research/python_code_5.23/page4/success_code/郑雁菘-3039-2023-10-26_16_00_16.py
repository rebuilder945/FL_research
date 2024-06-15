A = eval(input())
B = set(A)
m = max(B)
for i in A:
    if i == m:
        A.remove(i)
n = min(B)
for i in A:
    if i == n:
        A.remove(i)
print(A)



