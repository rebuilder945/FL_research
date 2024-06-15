s={"jishu":"red","oushu":"black"}
m={"jishu":"black","oushu":"red"}
n=int(input())
if n==0:
    print("green")
elif (n>=1 and n<=10) or (n>=19 and n<=28):
    if n%2==0:
        print(s["oushu"])
    else:
        print(s["jishu"])
elif (n>=11 and n<=18) or (n>=29 and n<=36):
    if n%2==0:
        print(m["oushu"])
    else:
        print(m["jishu"])
else:
    print("error")
#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303
