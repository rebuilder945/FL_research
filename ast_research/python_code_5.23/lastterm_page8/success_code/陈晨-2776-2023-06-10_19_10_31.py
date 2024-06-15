def  myFun(a,b):
       if float(a)%1==0 or float(b)%1==0:
           s="error"
           return s
       else:
           n=min([len(str(a)),len(str(b))])
           k=0
           for x in range(n):
               k+=str(a)[len(str(a))-1-x]*str(b)[len(str(b))-1-x]
           return k

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

