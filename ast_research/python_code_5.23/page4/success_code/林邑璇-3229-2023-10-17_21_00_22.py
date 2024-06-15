a=eval(input())
for i in a:
    b=a.count(i)
    if b==1:
        continue
    else:
        for x in range(a.count(i)):
            a.remove(i)
if len(a)==0:
    print("False")
else:
    print(a)

