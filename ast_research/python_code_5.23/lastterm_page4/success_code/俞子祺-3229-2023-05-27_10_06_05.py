ls=eval(input())
ls=list(ls)
ls1=[]
m=0
for x in ls:
   a=ls.count(x)
   if a==1:
      ls1.append(x)
      m+=1
ls1.sort()
if m!=0:
   print(ls1)
elif m==0:
   print("False")

