def  myFun(a,b):
           if abs(int(a))!=float(a) or abs(int(b))!=float(b):
               return ("error")
           else:
               areversed=a[::-1]
               breversed=b[::-1]
               if len(a)>len(b):
                   for i in range(len(a)-len(b)):
                       breversed=breversed+"0"
               elif len(a)<len(b):
                   for i in range(len(b)-len(a)):
                       areversed=areversed+"0"
               else:
                   pass
           sum=0
           for i in range(len(areversed)):
               sum+=int(areversed[i])*int(breversed[i])
           return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

