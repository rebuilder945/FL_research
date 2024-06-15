list = eval(input())
a = max(list)
b = min(list)
newl = []
for i in list:
    if i!=a and i!=b:
        newl.append(i)
print(newl)
