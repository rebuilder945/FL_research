a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
for x in range(b):
    a.remove(max(a))
if a!=[]:
    for x in range(c):
        a.remove(min(a))
else:
    pass
print(a)
    

