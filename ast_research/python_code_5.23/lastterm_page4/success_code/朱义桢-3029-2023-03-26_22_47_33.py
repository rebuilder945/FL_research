names=eval(input())
scores=eval(input())
names=list(names)
add=[]
for i in range(len(names)):
    a=[names[i],scores[i]]
    add.append(a)
print(add)
