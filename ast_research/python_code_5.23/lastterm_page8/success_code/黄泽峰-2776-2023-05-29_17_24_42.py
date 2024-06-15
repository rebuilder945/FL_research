def  myFun(a,b):
       lsa=[]
       a1= str(a)
       for i in range(len(a1)):
           lsa.append(a1[i-1])
       for i in lsa:
           jiji1*=int(i)
       lsb=[]
       b1= str(b)
       for i in range(len(b1)):
           lsa.append(b1[i-1])
       for i in lsb:
           jiji2*=int(i)
       return jiji1+jiji2

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

