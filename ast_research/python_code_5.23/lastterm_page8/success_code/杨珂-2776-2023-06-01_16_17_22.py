def  myFun(a,b):
       m=[]
       n=[]
       for i in a:
           m.append(i)
       for i in b:
           n.append(i)
       if len(m)>len(n):
           for i in range(len(n),len(m)):
               n.append("0")
       else:
           for i in range(len(m),len(n)):
               m.append("0")
       m.reverse()
       n.reverse()
       s=0
       for x,y in zip(m,n):
           s+=int(x)*int(y)
       return s
        

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

