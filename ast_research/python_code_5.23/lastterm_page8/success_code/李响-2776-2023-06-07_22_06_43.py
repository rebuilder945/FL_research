def  myFun(a,b):
       sum = 0
       a = str(a)
       b = str(b)
       if len(a) == len(b):
          for i in range(len(a)-1):
             m = int(a[i])
             n = int(b[i])
             s = m*n
             sum = s+sum
             return sum
       else:
          x = len(a) - len(b)
          if x >0:
             b = '0'*x+b
             myFun(a,b)
          else:
             a = '0'*(-x)+a
             myFun(a,b)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

