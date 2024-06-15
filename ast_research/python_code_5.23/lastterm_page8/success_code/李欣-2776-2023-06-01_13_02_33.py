def  myFun(a,b):
       n1=str(a)
       n2=str(b)
       s=0
       if len(n1)>len(n2):
            x=len(n1)-len(n2)
            for i in range(len(n2)):
                  s=s+int(n1[x+i])*int(n2[i])
            return s
       else:
            x=len(n2)-len(n1)
            for i in range(len(n1)):
                  s=s+int(n2[x+i])*int(n1[i])
            return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

