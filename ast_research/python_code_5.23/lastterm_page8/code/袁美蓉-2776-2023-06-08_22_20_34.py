def  myFun(a,b):
       a = list(a)
           b = list(b)
           if len(a)==len(b):
               for i in range(len(a)):
                   return sum(a[i]*b[i])
           elif len(a)>len(b):
               for i in range(len(b),1,-1):
                   return sum(a[i]*b[i])
           else:
               for i in range(len(a),1,-1):
                   return sum(a[i]*b[i])

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

