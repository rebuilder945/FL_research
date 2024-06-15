def  myFun(a,b):
       c=min(len(a),len(b))
       for i in range(1,c+1):
          d=[]
          a=int(a)
          b=int(b)
          d.append(a[i]*b[i])
       return sum(d)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

