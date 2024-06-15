list1=eval(input())
a=0
while len(list1)!=0:
    b=list1[0]
    jishu=0
    jishu1=0
    for x in list1:
        if x>b:
            b=x
            jishu1=jishu
            jishu+=1
            a=a*10+b
print(a)
