def  myFun(a,b):
       aa=list(map(int,str(a)))
       bb=list(map(int,str(b)))
       sum=0
       lenab=len(bb)-len(aa)
       if lenab>0:
           for i in range(abs(lenab)):
               aa.insert(0,0)
       elif lenab<0:
            for j in range(abs(lenab)):
               bb.insert(0,0)
       else:
           pass
       for k in range(lenab):
           sum+=aa[k]*bb[k]
       return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

