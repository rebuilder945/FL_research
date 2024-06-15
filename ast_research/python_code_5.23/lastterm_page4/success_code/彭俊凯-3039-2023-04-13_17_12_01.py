a=eval(input())
a.sort()
b=a[0]
for i in range(len(a)):
    if a[0]==b:
        a.remove(b)
    else:
        break
c=a[-1]
for i in range(len(a)):
    if a[-1]==c:
        a.remove(c)
    else:
        break
print(a)
