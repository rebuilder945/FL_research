names=input()
names=names.split(',')
scores=input()
scores=scores.split(',')
a=[]
for i in range(len(names)):
    a.append([names])
    a.append([scores])
    a=list(zip(names,scores))
print(a)

