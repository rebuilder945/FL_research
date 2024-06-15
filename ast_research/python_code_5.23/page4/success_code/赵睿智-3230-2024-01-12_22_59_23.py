a=eval(input())
b=[]
for i in a:
    m=a.count(i)
    if m==1:
        b.append(str(i))
b.sort()
if b==[]:
    print("False")
else:
    print(",".join(b))










             
