a=eval(input())
b=[]
for num in a:
    if a.count(num)==1:
        b.append(num)
if len(b)==0:
    print("False")
else:
    print(','.join(str(n) for n in b))
