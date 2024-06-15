def  myFun(a,b):
       c=len(a)
       d=len(b)
       lst=[]
       lst.append(c)
       lst.append(d)
       w=min(lst)
       e=0
       for i in range(w):
           e+=int(a.pop())*int(b.pop())
       return e


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

