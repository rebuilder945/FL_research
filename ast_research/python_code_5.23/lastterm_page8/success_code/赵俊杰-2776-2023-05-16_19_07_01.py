def  myFun(a,b):
       l1=len(a)
       l2=len(b)
       s=0
       if l1==l2:
          for x in a and y in b:
             s=s+int(x)*int(y)
       elif l1>l2:
          m=l1-l2
          for x in a[m:] and y in b:
             s=s+int(x)*int(y)
       else:
          m=l2-l1
          for x in a and y in b[m:]:
             s=s+int(x)*int(y)
       return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

