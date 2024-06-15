#第一种：
a = eval(input())
a.reverse()
b = []
for x in a:
    if x not in b:
        b.append(x)
        #b.append(a.pop(a.index(x)))
b.reverse()
print(b)
#第二种：
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






             
