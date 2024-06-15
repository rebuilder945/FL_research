def  myFun(a,b):
       a = a.zfill(max(len(a), len(b)))
       b = b.zfill(max(len(a), len(b)))
       res = sum([int(x) * int(y) for x, y in zip(a, b)])
       print(res)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

