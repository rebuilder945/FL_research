lst=eval(input())
a=[]
for i in range(-1,-len(lst),-1):
    if lst[i] not in a:
        a.append(lst[i])
a.reverse()
print(a)
