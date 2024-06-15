a=eval(input())
list1=[]
for x in a:
    b=a.count(x)
    if b==1:
        list1.append(x)
c=list1.count
if c==0:
    print("False")
else:
    print(list1)
