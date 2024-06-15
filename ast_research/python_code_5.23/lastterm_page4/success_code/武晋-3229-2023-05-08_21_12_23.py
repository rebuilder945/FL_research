lst=eval(input())
b=[]
for i in lst:
    if lst.count(i) == 1:
        b.append(i)
b.sort()
if b:
    print(",".join(str(i) for i in b))
else:
    print("False")
    



