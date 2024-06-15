lst=eval(input())
lst.reverse()
save=[]
for i in lst:
    if i not in save:
        save.append(i)
    else:
        pass
print(save.reverse())





# lst=eval(input())
# save=[]
# for i in range(len(lst)-1,-1,-1):
#     if lst[i] not in save:
#         save.append(lst[i])
# save.reverse()
# print(save)
