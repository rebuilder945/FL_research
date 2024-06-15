def  myFun(a,b):
           sums=0
           a1=len(a)
           b1=len(b)
           ls1=[]
           ls2=[]
           for i in a:
               ls1.append(int(i))
           for j in b:
               ls2.append(int(j))
           if a1==b1:
               for i in len(ls1):
                   sums+=ls1[i]*ls2[i]
           elif a1<b1:
               ls3=ls2[b1-a1:]
               for i in range(len(ls1)):
                   sums+=ls1[i]*ls3[i]
           elif a1>b1:
               ls4=ls1[a1-b1:]
               for i in range(len(ls2)):
                   sums+=ls4[i]*ls2[i]
           return sums

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

