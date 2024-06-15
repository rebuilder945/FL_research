n=eval(input())
l=[]
for num in n:
    if n.count(num)==1:
        l.append(num)
l.sort()
if l:
    print(",".join(str(i) for i in l))
else:
    print("False")

