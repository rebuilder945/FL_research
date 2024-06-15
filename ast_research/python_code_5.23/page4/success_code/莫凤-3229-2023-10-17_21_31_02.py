a=eval(input())
#s=''
list1=[]
for x in a:
    b=a.count(x)
    if b==1:
        list1.append(x)
        list1.sort()
        #s+=str(x)
c=list1.count
if c==0:
    print("False")
else:
    for i in list1:
        print(i)
