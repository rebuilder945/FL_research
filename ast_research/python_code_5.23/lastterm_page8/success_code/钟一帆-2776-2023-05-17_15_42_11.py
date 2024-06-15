def  myFun(a,b):
       c=len(a)-len(b)
       v=[]
       if c>=0:
           for i in range(len(a)):
               if i<c:
                   d=int(a[i:i+1])*0
               else: 
                   for x in range(len(b)):
                       if i-x==c:
                           d=int(a[i:1+i])*int(b[x:x+1])
                           v.append(d)
       return sum(v)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

