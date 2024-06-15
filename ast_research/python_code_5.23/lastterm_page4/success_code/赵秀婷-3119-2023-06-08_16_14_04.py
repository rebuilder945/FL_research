
lst=eval(input())
save=[]
for i in range(len(lst)-1,-1,-1):
    if lst[i] not in save:
        save.append(lst[i])
save.reverse()
print(save)
