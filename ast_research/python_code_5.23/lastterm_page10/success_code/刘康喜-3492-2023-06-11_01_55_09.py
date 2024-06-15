a=input()
b=0
for i in a:
   if a.count(i)==1:
      print(i)
      b=1
      break
if b==0:
   print('None')

