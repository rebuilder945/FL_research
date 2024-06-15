def zhishu(a):
    t=0
    for x in range(1,a):
        if a%x==0: t+=1
    if(t==1) :return 1
    else : return 0

ls1=eval(input())
ls2=[]
for i in ls1:
    #print(i,type(i))
    if zhishu(i) : ls2.append(i)
print(ls2)
