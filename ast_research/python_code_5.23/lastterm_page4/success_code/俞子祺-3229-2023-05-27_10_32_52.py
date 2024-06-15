ls=eval(input())
ls=list(ls)
ls1=[]
m=0
for x in ls:
   a=ls.count(x)
   if a==1:
      ls1.append(x)
      ls1.sort()
      m+=1
ls1=",".join(str(i) for i in ls1)
if m!=0:
   print(str(ls1))
elif m==0:
   print("False")
