lst=eval(input())
a = len(lst)
for i in range(a):
    if lst[i]!=0:
        i+=1
    elif lst[i]==0:
        del lst[i]
    lst.append(0)
print(lst)
