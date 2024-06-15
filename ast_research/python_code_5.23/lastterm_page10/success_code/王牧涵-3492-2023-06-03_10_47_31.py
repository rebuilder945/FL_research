a=input()
list=list(a)
jishu1=0
for x in list:
    jishu=0
    for x2 in list:
        if x==x2:
            jishu+=1
    if jishu==1:
        print(x)
        jishu1+=1
        break
    if jishu1==0:
        print("None")
