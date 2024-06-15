def  myFun(a,b):
       if type(eval(a))!=int or eval(a)<=0:
           return 'error'
       if type(eval(b))!=int or eval(b)<=0:
           return 'error'
       s=0
       for i in max(len(str(a)),len(str(b))):
           if a[i]=='' or b[i]=='':
               s+=0
           else:
               s+=int(a[i])*int(b[i])
       return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

