a=eval(input())
save=[]
for i in range(len(a)):
    if a[i] not in save:
        save.append(a[i])
print(save)
