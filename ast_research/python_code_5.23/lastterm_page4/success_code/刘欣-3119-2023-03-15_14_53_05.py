ls=eval(input())
newls=[]
for i in ls:
    if i not in newls:
        newls.append(i)
print(newls)
