def  myFun(a,b):
       if int(a)>0 and int(b)>0:   
           c=str(a)
           d=str(b)
           c=list(map(int,c))
           d=list(map(int,d))
           e=max(len(c),len(d))
           f=0
           for i in (1,e+1):
               f+=c[-i]*d[-i]
           return f
       else:
           return "error"

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

