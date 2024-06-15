def  myFun(a,b):
           a1=len(a)
           b1=len(b)
           if a1>=b1:
                shu=b1
           else:
                shu=a1 
           c=[]
           for x in range(1,shu+1):
               c1=int(b[-x])*int(a[-x])
               c.append(c1)
           return sum(c)     

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

