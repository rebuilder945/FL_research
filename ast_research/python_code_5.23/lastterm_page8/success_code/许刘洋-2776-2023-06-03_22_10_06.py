def  myFun(a,b):
       sum=0
       if eval(a)<=0 or eval(b)<=0:
           return error
       elif eval(a).isfloat() or eval(b).isfloat():
           return error
       else:
           while True:
               sum=sum+((eval(a)%10)*(eval(b)%10))
               a=eval(a)//10
               b=eval(b)//10
           return sum
               

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

