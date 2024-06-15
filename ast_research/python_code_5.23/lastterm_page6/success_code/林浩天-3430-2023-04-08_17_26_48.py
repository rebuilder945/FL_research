s={1:"spring",2:"summer",3:"autumn",4:"winter"}
n=int(input())
if(n>=3 and n<=5):
    print(s[1])
elif(n>=6 and n<=8):
    print(s[2])
elif(n>=9 and n<=11):
    print(s[3])
elif(n==12 or n==1 or n==2):
    print(s[4])
else:
    print("error")
#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303
