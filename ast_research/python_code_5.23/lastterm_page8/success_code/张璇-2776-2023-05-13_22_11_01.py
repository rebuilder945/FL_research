def  myFun(a,b):
           a=list(str(a))
           b=list(str(b))
           c=0
           if len(a)==len(b):
               for x in range(len(a)):
                   c=int(a[x])*int(b[x])+c
           elif len(a)>len(b):
               for x in range(-1,-len(a)):
                   c=int(a[x])*int(b[x])+c
           else :
               for x in range(-1,-len(b)):
                   c=int(a[x])*int(b[x])+c
           return c                 

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

