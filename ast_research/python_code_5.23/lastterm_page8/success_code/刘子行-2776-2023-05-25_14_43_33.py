def  myFun(a,b):
       if type(a)==int or type(b)==int:
           a1=[eval(x) for x in "a"]
           b1=[eval(x) for x in "b"]
           if len(a1)==len(b1):
               c=[x+y for x in a1 for y in b1]
               return sum(c)
           else:
               if len(a)>len(b):
                   n=len(a)-len(b)
                   c1=[0]*n
                   c2=c1+b
                   c3=[x+y for x in a1 for y in c2]
                   return sum(c3)
               else:
                   n1=len(b)-len(a)
                   c11=[0]*n
                   c22=c11+a
                   c33=[x+y for x in c22 for y in c2]
                   return sum(c33)
       else:
            return 'error'

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

