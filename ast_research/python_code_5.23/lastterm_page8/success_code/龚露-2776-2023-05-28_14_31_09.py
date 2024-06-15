def  myFun(a,b):
       if int(a)<0 or int(b)<0:
           return error
       elif len(a)==len(b):
           i=0
           while i < len(a):
               m=0
               m=m+a[i]*b[i]
               i = i+1
           return m
       elif len(a)>len(b):
           c=len(a)-len(b)
           i=0
           while i < len(b):
               m = 0
               m = m+a[c]*b[i]
               c=c+1
               i = i+1
           return m
       else:
           c=len(b)-len(a)
           i=0
           while i < len(a):
               m=0
               m = m+a[i]*b[c]
               c = c +1
               i = i+1
           return m


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

