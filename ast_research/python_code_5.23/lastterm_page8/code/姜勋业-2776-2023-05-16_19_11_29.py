def  myFun(a,b):
       k=0
       n=-1
       if a<=0 or b<=0:
          return error
       else:
          if len(str(a)<=len(str(b):
             for i in range(len(str(a)):
                   k+=int(str(a)[n])*int(str(b)[n])
                   n+=1
          else:
             for i in range(len(str(b)):
                   k+=int(str(a)[n])*int(str(b)[n])
                   n+=1
          return k

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

