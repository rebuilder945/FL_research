ls1=eval(input())
for i in range(len(ls1)):
    if ls1[i] == True and type(ls1[i]) == bool:
        ls1[i] = str(ls1[i])
y = ls1.copy
for x in y:
    if y.count(x) !=1:
        y.remove(i)
for i in range(len(x)):
    if x[i] == 'True':
        x[i] = eval(x[i])
print(x)
