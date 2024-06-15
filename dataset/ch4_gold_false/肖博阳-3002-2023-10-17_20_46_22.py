list1=eval(input())
total=0
for i in range(len(list1)):
    total+=list1[i]
a=total/len(list1)
if a==int:
   a2=int(a)
   print(a2)
else:
    print("%0.2f" % a)
       

