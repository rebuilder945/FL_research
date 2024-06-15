def  myFun(a,b):
           c=0
           a,b=int(a),int(b)
           n=max(len(str(a)),len(str(b)))
           for i in range(n):
               c=c+(a%10)*(b%10)
               a,b=a//10,b//10
           return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

