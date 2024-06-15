def  myFun(a,b):
           m,n=len(a),len(b)
           s=0
           if m>=n:
               ma=n
               for x in range(1,ma+1):
                   s+=int(a[-x])*int(b[-x])
               for x in a[0:m-n]:
                   s+=int(x)
               return(s)
           else:
               ma=m
               for x in range(1,ma+1):
                   s+=int(a[-x])*int(b[-x])
               for x in b[0:m-n]:
                   s+=int(x)
               return(s)   

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

