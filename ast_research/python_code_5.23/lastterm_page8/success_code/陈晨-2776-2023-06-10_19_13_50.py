def  myFun(a,b):
       
           n=min([len(str(a)),len(str(b))])
           k=0
           for x in range(n):
               k+=int(str(a)[len(str(a))-x])*int(str(b)[len(str(b))-x])
           return k

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

