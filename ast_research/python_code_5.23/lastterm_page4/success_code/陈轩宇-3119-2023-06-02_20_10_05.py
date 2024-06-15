a = eval(input())
save = []
a.reverse()
for i in a:
    if i not in save:
        save.append(i)
save.reverse()
print(save)
    
