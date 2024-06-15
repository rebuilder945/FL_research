def  myFun(a,b):
       a = str(a)
       b = str(b)
       c = [ ] 
       for i in a:
           i = int(i)
           for x in b:
               x = int(x)
               m = i*x
               c.append(m)
               break
       h = sum(c)-2
       return h

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

