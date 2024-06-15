def  myFun(a,b):
       if int(a)<0 or int(b)<0:
               return "error"
           else:
               a=list(a)
               b=list(b)
               a.reverse()
               b.reverse()
               sum=0
               if len(a)<len(b):
                   for x in range(len(a)):
                       sum+=int(a[x])*int(b[x])
               elif len(a)>len(b):
                   for x in range(len(b)):
                       sum+=int(a[x])*int(b[x])
               else:
                   for x in range(len(a)):
                       sum+=int(a[x])*int(b[x])
               return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

