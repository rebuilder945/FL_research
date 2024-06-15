def  myFun(a,b):
           m=0
           if len(a)>len(b):
               for i in range(len(b),0,-1):
                   m+=int(a[-i])*int(b[-i])
           else:
               for i in range(len(a),0,-1):
                   m+=int(a[-i])*int(b[-i])
           return m

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

