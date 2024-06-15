def  myFun(a,b):
       
           m=[x for x in str(a)]
           n=[x for x in str(b)]
           c=len(m)-len(n)
           s=0
           if c>0:
               n=[0]*c+n
               for x in len(n):
                   s+=int(m[x])*int(n[x])
               return s
           if c<0:
               m=[0]*c+m
               for x in len(m):
                   s+=int(m[x])*int(n[x])
               return s
           if c==0:
               for x in len(m):
                   s+=int(m[x])*int(n[x])
               return s
       else:
           return "error"

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

