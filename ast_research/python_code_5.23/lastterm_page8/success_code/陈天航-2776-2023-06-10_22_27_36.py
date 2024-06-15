def  myFun(a,b):
                  a=a[::-1]
                  b=b[::-1]
                  c=len(a)
                  d=len(b)
                  z=min(c,d)
                  e=0
                  for i in range(0,z):
                      e+=int(a[i])*int(b[i])
                  return e

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

