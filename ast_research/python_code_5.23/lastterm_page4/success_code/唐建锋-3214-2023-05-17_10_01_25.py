ls=eval(input())
for i in range(len(ls)):
    if ls[i]==0:
        ls.pop(i)
        ls.append(0)
print(ls)

