def  myFun(a,b):
           a1=str(a)
           b1=str(b)
           end=0
           if len(a1)<len(b1):
               len=len(a1)
           else:
               len=len(b1)
           for x in range(len):
               end+=int(a1[1-x])*int(b1[1-x])
               return end


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

