def  myFun(a,b):
           aa=list(a)
           bb=list(b)
           c=0
           if len(aa)==len(bb):
                   for i in range(len(aa)):
                       sum=int(aa[i])*int(bb[i])
                       c+=sum
                   return c
           elif len(aa)>len(bb):
               d=len(aa)-len(bb)
               for i in range(d):
                   bb.insert(0,0)
               for i in range(len(aa)):
                   sum=int(aa[i])*int(bb[i])
                   c+=sum
               return c
           else:
               d=len(bb)-len(aa)
               for i in range(d):
                   aa.insert(0,0)
               for i in range(len(aa)):
                   sum=int(aa[i])*int(bb[i])
                   c+=sum
               return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

