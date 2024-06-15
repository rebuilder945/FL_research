a=eval(input())
maxnum = max(a)
minnum = min(a)
for i in a[:]:
    if i == maxnum or i == minnum:
        a.remove(i)
print(a)
