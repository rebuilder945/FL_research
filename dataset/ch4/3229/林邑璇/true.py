a=eval(input())
for i in a:
    b=a.count(i)
    if b==1:
        continue
    else:
        for x in range(a.count(i)):
            a.remove(i)
a=sorted(a)
if len(a)==0:
    print("False")
else:
    b=','.join(str(i)for i in a)
    print(b)
