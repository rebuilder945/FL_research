lt=eval(input())
a=sum(lt)
b=len(lt)
c=a/b
if c==round(c):#判断c是不是整数
    print(c)
else:
    c=round(c,2)
    print(c)
