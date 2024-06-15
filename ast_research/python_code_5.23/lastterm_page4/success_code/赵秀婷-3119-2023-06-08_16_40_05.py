lst=eval(input())
save=[]
for i in lst[::-1]:
    if i not in save:
        save.append(i)
print(save.reverse())
