def  myFun(a,b):
       if int(a) <=0 or int(b) <= 0:
               return"error"
           else:
               a_list=list(a)
               a_list.reverse()
               b_list=list(b)
               b_list.reverse()
               pass
               if len(a_list)>len(b_list):
                   num=0
                   for x in list(range(len(b_list))):
                       num = num + (int(a_list[x])*int(str(b_list[x])))
               if len(a_list) < len(b_list):
                   num=0
                   for x in list(range(len(a_list))):
                       num = num + int(a_list[x])*int(str(b_list[x]))
               if len(a_list) == len(b_list):
                   num=0
                   for x in list(range(len(a_list))):
                       num = num + int(a_list[x])*int(str(b_list[x]))
               return num

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

