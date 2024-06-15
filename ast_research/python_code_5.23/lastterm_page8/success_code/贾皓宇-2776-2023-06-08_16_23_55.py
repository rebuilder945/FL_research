def  myFun(a,b):
               s=0
               a=str(a)
               b=str(b)
               if a<b:
                   for x in range(len(a)):
                       s=s+int(a[-x-1])+int(b[-x-1])
               else:
                   for x in range(len(b)):
                       s=s+int(a[-x-1])+int(b[-x-1])
               return s


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

