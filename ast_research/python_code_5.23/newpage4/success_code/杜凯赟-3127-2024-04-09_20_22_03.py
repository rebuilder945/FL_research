import numbers
n = eval(input())
list =[x for x in range(1,n+1)]
for i in range(1):
    a=list.pop(0)
    list.append(a)
print (list)
