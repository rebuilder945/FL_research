def  myFun(a,b):
       sum=0
           if len(a)<len(b):
               a="0"*(len(b)-len(a))+a
           else:
               b="0"*(len(a)-len(b))+b
           time=-1
           for x in a:
               time+=1
               n=int(x)*int(b[time])
               sum+=n
           return sum
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

