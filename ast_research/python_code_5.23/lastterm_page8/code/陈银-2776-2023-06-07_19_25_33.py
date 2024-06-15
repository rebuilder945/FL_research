def  myFun(a,b):
       if len(a)==len(b):
           m=0
           for x in range(len(a)):
               m+=int(a[x])*int(b[x])
               return m
       else:
           m=0
           if len(a)>len(b):
               q = len(a)-len(b) 
               b  = '0'*a+b
               for x in range(len(a)):
               m+=int(a[x])*int(b[x])
               return m
           else:
               q = len(b)-len(a) 
               a  = '0'*b+a
               for x in range(len(a)):
               m+=int(a[x])*int(b[x])
               return m        
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

