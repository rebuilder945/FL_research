def  myFun(a,b):
       a_str=str(a)[ : :-1]
       b_str=str(b)[ : :-1]
           min_len=min(len(a_str),len(b_str))
           result=0
           for i in range(min_len):
               result+=int(a_str[i]*int(b_str))
           if len(a_str)>len(b_str):
               result+=sum(int(a_str[i])for i in range(min_len,len(a_str)))
           else:
               result+=sum(int(b_str[i])for i in range(min_len,len(b_str)))
           return result

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

