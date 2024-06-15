names=input().split(",")
scores=eval(input())
add=[]
for i in range(0,len(names)):
    a=[names[i],scores[i]]
    add.append(a)
print(add)
