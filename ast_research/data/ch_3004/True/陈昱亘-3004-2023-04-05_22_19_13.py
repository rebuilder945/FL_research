lst=eval(input())
lst2=[]
lst3=[]
for i in range(len(lst)):
    for x in range(lst[i]):
        if lst[i]%(x+1)==0:
            lst2.append(x+1)
    if lst2==[1,lst[i]]:
        lst3.append(lst[i])
    lst2=[]
print(lst3)
