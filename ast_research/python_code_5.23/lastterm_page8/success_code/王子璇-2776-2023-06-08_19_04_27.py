def  myFun(a,b):
           a=list(str(a));b=list(str(b))
           a=list(map(int,a));b=list(map(int,b))
           a.reverse();b.reverse()
           number=0
           for x in range(min(len(a),len(b))):
               number+=a[x]*b[x]
           return number

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

