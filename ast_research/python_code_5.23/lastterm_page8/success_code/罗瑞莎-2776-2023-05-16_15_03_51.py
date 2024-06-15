def  myFun(a,b):
       lsta = []
       lstb = []
       n = 0
       if int(a)>0 and int(b)>0 and (float(a)-int(a))==0 and (float(b)-int(b))==0:
           for i in range(len(a)):
               lsta.insert(0,a[i])
           for j in range(len(b)):
               lstb.insert(0,b[i])
           if len(a) > len(b):
               for k in range(len(b)):
                   n += eval(lsta[k])*eval(lstb[k])
               return n
           if len(a) < len(b):
               for k in range(len(a)):
                   n += eval(lsta[k])*eval(lstb[k])
               return n
       else:
           print("error")
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

