a=eval(input())
b=eval(input())
jishu1=eval('red')
jishu2=eval('blue')
jishu3=eval('yellow')
if a==b:
    print("error")
elif a==jishu1 and b==jishu2:
    print("purple")
elif a==jishu1 and b==jishu3:
    print("orange")
elif a==jishu2 and b==jishu3:
    print("green")
else:
    print("error")
