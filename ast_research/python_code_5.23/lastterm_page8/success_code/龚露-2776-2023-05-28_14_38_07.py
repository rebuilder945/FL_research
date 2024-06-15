def  myFun(a,b):
       if len(a)==len(b):
           i=0
           m=0
           while i < len(a):
               m=m+int(a[i])*int(b[i])
               i = i+1
           return m
       elif len(a)>len(b):
           c=len(a)-len(b)
           i=0
           m=0
           while i < len(b):
               m = m+int(a[c-1])*int(b[i])
               c=c+1
               i = i+1
           return m
       else:
           c=len(b)-len(a)
           i=0
           m=0
           while i < len(a):
               m = m+int(a[i])*int(b[c-1])
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

