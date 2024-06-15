x = eval(input())
for i in range(len(x)):
    if x[i] == True and type(x[i]) == bool:
        x[i] = str(x[i])
y = x.copy()
for i in y:
    if x.count(i) != 1:
        x.remove(i)
for i in range(len(x)):
    if x[i] == 'True':
        x[i] = eval(x[i])
print(x)

