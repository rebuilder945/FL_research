n=eval(input())
ls=[]
for i in range(len(n)):
    if n[i] not in n[i+1:]:
        ls.append(n[i])
print(ls)
