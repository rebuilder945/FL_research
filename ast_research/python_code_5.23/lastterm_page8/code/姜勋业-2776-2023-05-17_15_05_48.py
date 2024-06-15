def  myFun(a,b):
       c=len(a)
       d=len(b)
       sum=0
       if c>=d:
          for i in range(d):
               sum+=int(a[-i-1])*int(b[-i-1])
       else:
          for i in range(c)
               sum+=int(a[-i-1])*int(b[-i-1])
       return sum
         

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

