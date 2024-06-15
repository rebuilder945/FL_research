s={"red":1,"blue":2,"yellow":3}
s1=input()
s2=input()
sum=s.get(s1,10)+s.get(s2,10)
if sum==3:
    print("purple")
elif sum==4:
    print("orange")
elif sum==5:
    print("green")
else:
    print("error")
#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303
