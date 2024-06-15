# #11
# def    myFun(a,b):
#     if eval(a)<=0 or eval(b)<=0 or int(a)!=float(a) or int(b)!=float(b):
#         return 'error'
#     else:
#         s=min(len(a),len(b))
#         n=0
#         for i in range(1,s+1):
#             n+=int(a[-i])*int(b[-i])
#         return n
# num=input().split()
# a=num[0]
# b=num[1]
# if  a.isdigit()  and  b.isdigit():  #判断a,b是否都是数字
#               print(myFun(a,b))    #调用自定义函数
# else:
#               print("error")

'''-------------------------------------------------------------------------------------------------------------------------------'''

#1
a = input().split(',')
b = input().split(',')
for e in b:
    e=eval(e)
c=[]
for i in range(len(a)):
    c.append([b[i],a[i]])
c.sort()
for x in range(len(c)):
    m,n=c[x][0],c[x][1]
    c[x][0],c[x][1]=n,m
print(c)
