a=eval(input())
A=max(a)
B=min(a)
x=a.count(B)
d=a.count(A)
for i in range(x):
    a.remove(B)
for i in range(d):
    a.remove(A)
print(a)

