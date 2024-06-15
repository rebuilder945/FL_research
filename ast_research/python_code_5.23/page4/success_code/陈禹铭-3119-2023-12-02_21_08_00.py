
list1 = eval(input())
ls=[]
i=len(list1)-1
while i>=0:
    if list1[i] not in ls:
        ls.append(list1[i])
    i-=1 
print(ls)





