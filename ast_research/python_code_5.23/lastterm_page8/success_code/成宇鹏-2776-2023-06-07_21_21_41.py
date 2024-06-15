def  myFun(a,b):
           a = list(map(int,a))
           b = list(map(int,b))
           a.reverse()
           b.reverse()
           i = 0
           if len(a) < leb(b):
               a += [0]*(len(b)-len(a))
               for x in range(len(a)):
                   i += a[x]*b[x]
           elif len(a) > leb(b):
               b += [0]*(len(a)-len(b))
               for x in range(len(a)):
                   i += a[x]*b[x]
           else:
               for x in range(len(a)):
                   i += a[x]*b[x]
           return i

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

