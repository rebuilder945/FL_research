def  myFun(a,b):
           plist = []
           length = min(len(a),len(b))
           for i in range(-1, -length - 1, -1):
               tim = int(a[i]) * int(b[i])
               plist.append(tim)
           return sum(plist)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

