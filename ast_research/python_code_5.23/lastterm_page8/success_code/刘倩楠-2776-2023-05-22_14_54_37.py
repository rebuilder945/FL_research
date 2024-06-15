def  myFun(a,b):
       if int(a)<=0 or int(b)<=0:
           return error
       s=0
       ls1=list(a)
       ls2=list(b)
       if len(ls1)>len(ls2):
           n=len(ls1)-len(ls2)
           lt2=[0]*n
           ls2=lt2+ls2
           for i in range(len(ls2)):
               s+=int(ls1[i])*int(ls2[i])
       elif len(ls2)>len(ls1):
           m=len(ls2)-len(ls1)
           lt1=[0]*m
           ls1=lt1+ls1
           for j in range(len(ls2)):
               s+=int(ls1[j])*int(ls2[j])
       else:
           for i in range(len(ls1)):
               s+=int(ls1[i])*int(ls2[i])
       return s


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

