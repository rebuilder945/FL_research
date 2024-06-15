names=input("")
names=names.split(',')
scores=input()
a=[]
for i in range(len(names)):
    a.append([names[i],scores[i]])
print(a)

