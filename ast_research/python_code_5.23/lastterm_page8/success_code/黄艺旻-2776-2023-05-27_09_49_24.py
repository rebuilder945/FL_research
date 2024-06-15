def  myFun(a,b):
       m=[]
       a=str(a)
       b=str(b)
       if len(a)==len(b):
           for i in range(len(a)):
               n=int(a[i])*int(b[i])
               m.append(n)
           return sum(m)
       elif len(a)<len(b):
           c=a[::-1]
           d=b[::-1]
           for j in range(len(a)):
               n=int(c[j])*int(d[j])
               m.append(n)
           return sum(m)
       else:
           c=a[::-1]
           d=b[::-1]
           for j in range(len(b)):
               n=int(c[j])*int(d[j])
               m.append(n)
           return sum(m)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

