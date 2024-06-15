def  myFun(a,b):
               a1=[]
               b1=[]
               sum1=[]
               for i in a:
                   i=int(i)
                   a1.append(i)
               a1.reverse()
               for i in b:
                   i=int(i)
                   b1.append(i)
               b1.reverse()
               for i in range(min(len(a),len(b))):
                   sumi=a1[i]*b1[i]
                   sum1.append(sumi)
               return sum(sum1)


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

