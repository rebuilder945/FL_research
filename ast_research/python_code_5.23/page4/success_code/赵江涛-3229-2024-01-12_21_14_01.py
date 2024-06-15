a = eval(input())
for x in a:
    if a.count(x)>1:
        for i in range(a.count(x)):
            a.remove(x)
a.sort()
s = ",".join(str(i)for i in a)
if len(a)>0:
   
    print(a)
else:
    print("False")
