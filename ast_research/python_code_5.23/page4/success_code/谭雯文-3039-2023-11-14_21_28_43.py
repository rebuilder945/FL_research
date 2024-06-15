a=eval(input())
# b=max(a)
# c=min(a)
a.sort()
n1=a.count(a[0])
n2=a.count(a[-1])
for i in range(n1):
    a.remove(a[0])
for x in range(n2):
    a.remove(a[-1])
print(a)

