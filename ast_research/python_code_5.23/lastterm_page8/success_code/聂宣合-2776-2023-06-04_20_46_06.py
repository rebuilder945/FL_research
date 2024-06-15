def  myFun(a,b):
           if float(a)>0 and float(b)>0 and (int(a))%1==0 and (int(a))%1==0:
               sums=0
               a=str(a)
               b=str(b)
               if len(str(a))==len(str(b)):
                   for i in range(0,len(str(a))):
                       sums+=(int(a[i]))*(int(b[i]))
               if len(str(a))>len(str(b)):
                   x=len(str(a))-len(str(b))
                   b="0"*x+str(b)
                   for i in range(0,len(str(a))):
                       sums+=(int(a[i]))*(int(b[i]))
               if len(str(a))<len(str(b)):
                   x=len(str(b))-len(str(a))
                   a="0"*x+str(a)
                   for i in range(0,len(str(b))):
                       sums+=(int(a[i]))*(int(b[i]))
               return(sums)
           else:
               return("error")

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

