a=eval(input())
b=[]
for i in range(0,len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
if b==[]:
    print("False")
else:
    print(b)
