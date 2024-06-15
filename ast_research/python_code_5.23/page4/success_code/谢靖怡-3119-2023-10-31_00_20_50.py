ls1=eval(input())
for i in range(len(ls1)):
    if ls1[i] == True and type(ls1[i]) == bool:
        ls1[i] = str(ls1[i])
y = ls1.copy
for a in y:
    if ls1.count(a) !=1:
        ls1.remove(a)
for i in range(len(ls1)):
    if ls1[i] == 'True':
        ls1[i] = eval(ls1[i])
print(ls1)
