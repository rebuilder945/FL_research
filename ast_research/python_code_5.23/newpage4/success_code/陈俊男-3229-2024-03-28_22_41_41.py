a=eval(input())
b=[]
for num in a:
    if a.count(num)==1:
        b.append(num)
if b==0:
    print("False")
else:
    print(sorted(b))
