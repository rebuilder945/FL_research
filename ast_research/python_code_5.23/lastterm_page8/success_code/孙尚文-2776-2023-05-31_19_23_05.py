def  myFun(a,b):
           a=eval(a)
           b=eval(b)
           if type(a)!=int or type(b)!=int or a%1!=0 or b%1!=0 or a<0 or b<0:
               return "error"
           a=str(a)
           b=str(b)
           c=0
       
           if len(a)==len(b):
               for i in range(len(a)):
                   c+=int(a[i])*int(b[i])
               return c
           elif len(a)<len(b):
               for i in range(len(a)):
                   c+=int(a[i])*(int(b[i+len(b)-len(a)]))
               return c
           elif len(a)>len(b):
               for i in range(len(b)):
                   c+=(int(a[i+len(a)-len(b)]))*int(b[i])
               return c


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

