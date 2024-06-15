def  myFun(a,b):
        l=0
       if len(a)<len(b):
           s=b[1:len(b)]
           for x in range(0,len(a)):
               for y in range(0,len(s)):
                   if x==y:
                        l=l+int(a[x])*int(s[y])
           return l
       elif len(a)>len(b):
           s=a[1:len(a)]
           for x in range(0,len(b)):
               for y in range(0,len(s)):
                    if x==y:
                       l=l+int(b[x])*int(s[y])
           return l   

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

