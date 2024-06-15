lst=eval(input())
da=max(lst)
xiao=min(lst)
for i in range(len(lst)):
    if lst[i]==da or lst[i]==xiao:
        lst.remove(lst[i])
    else:
        continue
print(lst)
