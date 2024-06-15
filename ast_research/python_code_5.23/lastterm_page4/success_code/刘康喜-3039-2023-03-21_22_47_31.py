a=eval(input())
b=a.copy()
for i in range(0,len(a)):
    if a[i]==min(a) or a[i]==max(a):
        b.remove(a[i])
print(b)

