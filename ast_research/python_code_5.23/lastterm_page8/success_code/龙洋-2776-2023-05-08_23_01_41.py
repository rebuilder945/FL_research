def  myFun(a,b):
       l1=len(a)
       l2=len(b)
       l3=min(l1,l2)
       for n in range(l3):
        q=q+int(a[-n-1])*int(b[-n-1])
       return q

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

