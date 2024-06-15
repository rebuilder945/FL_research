num=[]
lst=eval(input())
i=2
for i in lst:
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)

