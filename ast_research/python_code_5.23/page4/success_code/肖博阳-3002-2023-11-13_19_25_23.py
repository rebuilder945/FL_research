list1=eval(input())
total=0
for i in list1:
    total+=i
a=total/len(list1)
b=a-int(a)
if b==0:

   print("%d" % a)
else:
    print("%.2f" % a)
       


