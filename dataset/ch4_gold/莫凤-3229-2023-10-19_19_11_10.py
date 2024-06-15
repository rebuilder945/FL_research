a=eval(input())
s=''
list1=[]
for x in a:
    b=a.count(x)
    if b==1:
        list1.append(x)
        list1.sort()
c=len(list1)
for y in list1:
    s+=str(y)
if c==0:
    print("False")
else:
    print(",".join(map(str,list1)))
