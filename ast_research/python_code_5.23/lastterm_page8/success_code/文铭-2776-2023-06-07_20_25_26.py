def  myFun(a,b):
       if a >0 and b>0:
           a =str(a)
           b = str(b)
           js =0
           n1 = len(a)
           n2 = len(b)
           if n1>n2:
               n2 = ln
           else:
               n1 = ln
           for x in range(-1,-ln-1,-1):
                js +=int(a[x])*int(b[x])
           return js
       else:
           return "error"

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

