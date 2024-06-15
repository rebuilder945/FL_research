A=eval(input())
a=max(A)
b=min(A)
A1=A.copy()
for i in A:
    if i == a or i == b:
        A1.remove(i)
print(A1)
