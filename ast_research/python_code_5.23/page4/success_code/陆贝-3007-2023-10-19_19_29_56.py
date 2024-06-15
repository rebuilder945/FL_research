ls=eval(input())
cd=len(ls)
a,b=eval(input())
if a>=b:
    print("error")
elif a>=cd:
    print("error")
elif b>=cd:
    print("error")
else:
    #lt=ls[a:b]
    #ii=ls-lt 错误操作
    del ls[a:b]
    print(ls)
    #print(ls)不然没有返回值

