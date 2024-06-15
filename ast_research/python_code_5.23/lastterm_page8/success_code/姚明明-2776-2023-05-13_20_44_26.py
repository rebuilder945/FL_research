def  myFun(a,b):
       if len(a)==len(b):
           for i in range(0,len(a)):
               lst=[]
               m=a[i]*b[i]
               lst.append(m)
               n=sum(lst)
       elif len(a)!=len(b):
           c=max(a,b)
           d=min(a,b)
           for i in range(-len(d),0):
               lst1=[]
               m=c[i]*d[i]
               lst1.append(m)
               n=sum(lst1)
       return n
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

