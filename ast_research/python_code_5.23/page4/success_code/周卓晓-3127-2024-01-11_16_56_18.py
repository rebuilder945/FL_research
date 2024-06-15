lst=[x for x in range(1,eval(input())+1)]
lst.append(lst[0])
for i in range(len(lst)):
    lst[i-1]=lst[i]
del lst[-1]
print(lst)


