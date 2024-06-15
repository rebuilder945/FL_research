def  myFun(a,b):
       c=0
       if len(a)>len(b):
           while len(b)!=len(a):
               b='0'+b
       if len(a)<len(b):
           while len(b)!=len(a):
               a='0'+a
       for i in range(len(a)):
           c+=int(a[i])*int(b[i])
       return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

