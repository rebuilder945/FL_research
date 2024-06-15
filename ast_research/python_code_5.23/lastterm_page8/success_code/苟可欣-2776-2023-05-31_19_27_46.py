def  myFun(a,b):
       al=[]
       bl=[]
       k=0
       for x in a:
           al.append(x)
       for x in b :
           bl.append(x)
       for x in range(len(bl)):
           b=(int(al[i])*int(bl[i]))
           if x==len(bl)-1 or x==len(al)-1:
               break
       print(k)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

