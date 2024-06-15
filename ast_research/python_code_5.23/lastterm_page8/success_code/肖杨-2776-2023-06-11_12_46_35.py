def  myFun(a,b):
                  l=max(len(a),len(b))
                  m=[]
                  c=0
                  for i in range(2):
                      m.append([0]*l)
                  for x in range(len(a)):
                      m[0][-1-x]=a[-1-x]
                  for x in range(len(b)):
                      m[1][-1-x]=b[-1-x]
                  for i in range(l):
                      c+=int(m[0][i])*int(m[1][i])
                  return c


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

