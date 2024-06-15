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
    for i in range(len(a)):
        print(a[i],end=",")
