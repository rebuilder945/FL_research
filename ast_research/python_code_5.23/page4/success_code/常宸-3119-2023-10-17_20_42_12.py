a = eval(input())
save = []
for i in range(len(a)-1,-1,-1):
    if a[i] not in save:
        save.append(a[i])
save.revelse()
print(save)
