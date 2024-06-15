n=eval(input())
n1=n
jishu1=2
jishu2=3
jishu3=1
jishu4=2
eva=jishu1/1+jishu2/2
while n-2>0:
    eva+=(jishu1+jishu2)/(jishu3+jishu4)
    jishu1,jishu2=jishu2,jishu1+jishu2
    jishu3,jishu4=jishu4,jishu3+jishu4
    n-=1
if n1==0:
    print(0)
elif n1==1:
    print("%.4f"%jishu1)
elif n1==2:
    print("%.4f"%(jishu1/1+jishu2/2))
elif n1>=3:
    print("%.4f"%eva)
