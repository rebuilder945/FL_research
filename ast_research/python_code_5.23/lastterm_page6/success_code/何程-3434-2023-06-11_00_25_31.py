a=input()
b=input()
jishu1='red'
jishu2='blue'
jishu3='yellow'
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
