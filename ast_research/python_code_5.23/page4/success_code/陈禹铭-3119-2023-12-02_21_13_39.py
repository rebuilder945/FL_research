
list1 = eval(input())
ls=[]
i=len(list1)-1
while i>=0:
    if list1[i] not in ls:
        ls.append(list1[i])
    i-=1
ls2=[]
h=len(ls)-1
while h>=0:
    ls2.append(ls[h])
    h-=1
print(ls2)





