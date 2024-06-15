lt=eval(input())
a=sum(lt)
b=len(lt)
c=a/b
if c==round(c):#判断c是不是整数
    c=round(c)
    print(c)#只是判断了忘记给c进行重新赋值
else:
    print("%.2f"%c)
