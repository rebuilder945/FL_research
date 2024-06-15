from itertools import count 
a=eval(input())
for i in range(len(a)):
    b=a.count(a[i])
    if b==1:
        continue
    else:
        del a[i]
        a.insert(i,"$")
while "$" in a:
    a.remove("$")
print(a)
