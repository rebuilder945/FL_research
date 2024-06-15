lst = eval(input())
a = lst.count(0)
while lst.count(0)>0:
    lst.remove(0)
b = [0]*a
lst = lst + b
print(lst)
