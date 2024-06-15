a=input()
lst=[a]
while a!='#' :
    a=input()
    lst.append(a)
del lst[-1]
print(lst)
print(len(lst),end=" ")
for i in range(len(lst)):
    lst[i]=int(lst[i])
print(sum(lst))
