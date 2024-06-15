def  myFun(a,b):
           m=len(a)
           n=len(b)
           if m==n:
               k=0
               for h in range(m):
                   k+=int(a[h])*int(b[h])
               return k
           elif m<n:
               k=0
               a='0'*(n-m)+a
               for h in range(n):
                   k+=int(a[h])*int(b[h])
               return k
           else:
               k=0
               b='0'*(n-m)+b
               for h in range(n):
                   k+=int(a[h])*int(b[h])
               return k

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

