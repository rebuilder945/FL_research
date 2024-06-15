def  myFun(a,b):
       if len(a)>len(b):
           n=(int(len(a))-int(len(b)))*str(0)
           c=str(n)+str(b)
           d=0
           for i in range(len(a)):
               d+=int(a[i])*int(c[i])
           return(d)
       if len(a)<len(b):
           m=(int(len(b))-int(len(a)))*str(0)
           p=str(m)+str(a)
           e=0
           for i in range(len(b)):
               e+=int(p[i])*int(b[i])
           return(e)
       if len(a)==len(b):
           u=0
           for i in range(len(b)):
               u+=int(a[i])*int(b[i])
           return(u)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

