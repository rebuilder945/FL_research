a=input()
lst=[a]
while a!='#' :
    a=input()
    lst.append(a)
del lst[-1]
print(lst)
print(len(lst),end=" ")
print(sum(lst))
