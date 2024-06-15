def  myFun(a,b):
       if a<0 or b<0:
           return "error"
       else:
           if len(a)==len(b):
               s=0
               for i in range(len(a)):
                   s=s+int(a[i])*int(b[i])
               return s
           elif len(a)>len(b):
               s=0
               for i in range(len(b),0,-1):
                   s=s+int(a[i])*int(b[i])
               return s
           else:
               s=0
               for i in range(len(a),0,-1):
                   s=s+int(a[i])*int(b[i])   
               return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

