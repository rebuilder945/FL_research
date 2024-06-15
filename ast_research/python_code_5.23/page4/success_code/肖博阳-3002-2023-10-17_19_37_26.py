list1=eval(input())
total=0
for i in range(len(list1)+1):
    total+=i
a=total/len(list1)
if a==int:

   print(a)
else:
    print("%0.2f" % a)


