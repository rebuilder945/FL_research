a=eval(input())
b=a.copy()
for i in b:
    c=b.count(i)
if c>1:
    for i in range(c-1):
        a.remove(i)
print(a)

