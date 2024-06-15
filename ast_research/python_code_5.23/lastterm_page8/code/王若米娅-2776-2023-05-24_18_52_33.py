def  myFun(a,b):
       s1=[]
       ls2=[]
       for x in a:
           ls1.append(eval(x))
       for x in b:
           ls2.append(eval(x))
       if len(ls1)>len(ls2):
           c=len(ls1)-len(ls2)
           ls2=[0]*c+ls2
       elif len(ls2)>len(ls1):
           c=len(ls2)-len(ls1)
           ls1=[0]*c+ls1
       sum=0
       for x in range(len(ls1)):
               sum+=ls1[x]*ls2[x]
           return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

