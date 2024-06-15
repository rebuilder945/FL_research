def weishu(x):
    jishu=0
    while x>1:
        x/=10
        jishu+=1
    return jishu

def shuixianhua(x):
    jishu=weishu(x)
    n=x
    eva=0
    while n>0:
        eva+=(n%10)**jishu
        n=int(n/10)
    if eva==x:
        return x
    else:
        return 0

a=eval(input())
a=list(range(100,a+1))
jishu=0
lst1=[]
for x in a:
    if shuixianhua(x)==0:
        continue
    elif shuixianhua(x)!=0 and shuixianhua(x)<1000:
        jishu+=1
        lst1.append(x)
if jishu==0:
    print("none")
else:
    i=0
    while jishu>0:
        print("{}".format(lst1[i]))
        i+=1
        jishu-=1




