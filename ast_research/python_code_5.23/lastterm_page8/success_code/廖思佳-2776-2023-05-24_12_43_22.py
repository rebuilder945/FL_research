def  myFun(a,b):
           while len(a)!=len(b):
               if len(a)<len(b):
                   a="0"+a
               if len(a)>len(b):
                   b="0"+b
           s=0        
           for i in range(len(a)):
               s=s+int(a[i])*int(b[i])
           return s    

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

