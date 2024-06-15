lst=eval(input())
da=max(lst)
xiao=min(lst)
for i in range(len(lst)-1):
    if lst[i]==da or lst[i]==xiao:
        lst.remove(lst[i])
    else:
        pass
print(lst)
