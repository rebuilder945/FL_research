def  myFun(a,b):
       a=eval(a)
       b=eval(b)
       if type(a)==type(1) and type(b)==type(1) and a>0 and b>0:
           if a>b:
               c=len(str(a))-len(str(b))
               b='0'*c+str(b)
               a=str(a)
               list0=[]
               for i in range(len(a)):
                   d=int(a[i])*int(b[i])
                   list0.append(d)
               e=0
               for i in range(len(list0)):
                   e=e + list0[i]
               return e
           else:
               c=len(str(b))-len(str(a))
               b='0'*c+str(a)
               b=str(b)
               list0=[]
               for i in range(len(b)):
                   d=int(a[i])*int(b[i])
                   list0.append(d)
               e=0
               for i in range(len(list0)):
                   e=e + list0[i]
               return e
       else:
           return 'error'

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

