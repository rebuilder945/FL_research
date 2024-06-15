a=eval(input())
import copy
c=copy.deepcopy(a)
for x in a:
    b=a.count(x)
    if b>=2:
        for i in range(b-1):
            a.remove(x)
            c.remove(x)
print(c)
