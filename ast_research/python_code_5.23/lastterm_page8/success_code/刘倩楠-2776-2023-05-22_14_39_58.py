def  myFun(a,b):
       s=0
       ls1=list(a)
       ls2=list(b)
       if len(ls1)>len(ls2):
           n=len(ls1)-len(ls2)
           ls2.insert(0,0*n)
           for i in range(len(ls1)):
               s+=ls1[i]*ls2[2]
       elif len(ls2)>len(ls1):
           m=len(ls2)-len(ls1)
           ls1.insert(0,0*m)
           for j in range(len(ls2)):
               s+=ls1[j]*ls2[j]
       else:
           for i in range(len(ls1)):
               s+=ls1[i]*ls2[i]
       return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

