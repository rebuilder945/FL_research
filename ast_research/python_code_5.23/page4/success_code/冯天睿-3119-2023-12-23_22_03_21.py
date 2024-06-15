
import copy
a = eval(input())
b = copy.deepcopy(a)
for x in a:
    if a.count(x)>1:
        for i in range((a.count(x))-1):
            b.remove(x)
    else:
        break
print(b)

