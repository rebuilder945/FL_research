def  myFun(a,b):
       c=0
       if len(a)==len(b):
           for i in a:
               for x in b:
                   c+=a*b

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

