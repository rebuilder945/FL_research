m=input()                                  #输入模块
n=input()
m=m.split(",")
n=n.split(",")
a1=float(n[0])                                #转型模块
a2=float(n[1])
a3=float(m[0])
a4=float(m[1])
length=((a1-a3)**2+(a2-a4)**2)        #计算模块
last=length**0.5
stext="%.2f"%(last)                        #转义模块
print(stext)                                #打印模块
