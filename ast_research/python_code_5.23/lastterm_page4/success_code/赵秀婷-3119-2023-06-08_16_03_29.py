lst=eval(input())
lst.reverse()
save=[]
for i in range(0,len(lst)-1):
    if i not in save:
        save.append(i)
print(save.reverse())
