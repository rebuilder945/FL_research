a=input()
list1=list(a)
jishu1=0
for x in list1:
    jishu=0
    for x2 in list1:
        if x==x2:
            jishu+=1
    if jishu==1:
        print(x)
        jishu+=1
if jishu1==0:
    print("None")
