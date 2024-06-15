a = eval(input())
import copy
b = copy.deepcopy(a)
for num1 in a:
    if b.count(num1) > 1:
        num2 = a.count(num1)-1
        num3 = a.index(num1)
        for i in range(num2):
            del b[num3]
    else:
        pass
print(b)

