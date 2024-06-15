A=eval(input())
a=max(A)
b=min(A)
for i in A:
    if i == a or i == b:
        A.remove(i)
print(A)
