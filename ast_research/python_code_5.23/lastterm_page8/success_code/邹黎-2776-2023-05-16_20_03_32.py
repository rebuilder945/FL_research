def  myFun(a,b):
       
       
           total=0
           a=str(a)
           b=str(b)
           if len(a)==len(b):
               for x in range(0,len(a)):
                   total+=int(a[x])*int(b[x])
           
           if len(a)>len(b):
               a=a[int(len(a)-len(b)):]
               for x in range(0,len(a)):
                   total+=int(a[x])*int(b[x])
           if len(b)>len(a):
               b=b[int(len(b)-len(a)):]
               for x in range(0,len(a)):
                   total+=int(a[x])*int(b[x])    
           return total

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

