lst=eval(input())
a=lst.count(0)
for i in range(a):
    a.append(0)
for i in range(a):
    a.remove(0)        
print(a)
