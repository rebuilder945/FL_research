names=input("")
names=names.split(',')
scores=input()
scores=scores.split(',')
a=[]
for i in range(len(names)):
    a.append([names[i],scores[i]])
print(a)

