def  myFun(a,b):
       sum=0
       a=list(a)
       b=list(b)
       while len(a):
           while len(b):
               sum += int(a.pop())*int(b.pop())
           break
       return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

