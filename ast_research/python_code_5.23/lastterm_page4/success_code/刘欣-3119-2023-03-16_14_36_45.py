ls=eval(input())
newls=[]
for i in ls:
    if i not in newls:
        for i in range(len(newls)):
            newls.append(i)
print(newls)
