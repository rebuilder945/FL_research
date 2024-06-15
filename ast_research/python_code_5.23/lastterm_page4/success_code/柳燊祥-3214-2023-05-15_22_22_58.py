lst=eval(input())
x=lst.count(0)
p=0
while p<x:
    lst.remove(0)
    p+=1
q=0
while q<x:
    lst.append(0)
    q+=1
print(lst)
