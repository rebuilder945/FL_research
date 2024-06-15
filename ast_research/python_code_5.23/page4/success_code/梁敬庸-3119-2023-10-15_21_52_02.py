a=eval(input())
for i in a:
    if a.count(i)>1:
       for x in range(a.count(i)-1):
           del a[a.index(i)]
print(a)        

