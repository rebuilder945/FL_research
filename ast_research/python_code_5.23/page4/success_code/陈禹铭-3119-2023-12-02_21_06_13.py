
list1 = eval(input())
ls=[]
i=len(list1)
while i>=0:
    if list1[i] not in ls:
        ls.append(list1[i])
    i-=1 
ls.sort()   
print(ls)





