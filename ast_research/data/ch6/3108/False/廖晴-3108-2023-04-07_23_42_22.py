s=eval(input())
a="".join(s)
for i in a:
    if i not in s:
        s.append(i)
        s.sort()
for x in s:
    if len(x)==1:
        print(x,a.count(x))
