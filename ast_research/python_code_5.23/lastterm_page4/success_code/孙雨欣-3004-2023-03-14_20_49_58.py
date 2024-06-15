def sushu(num):
    y=True
    if num==1:
        y=False
    for i in range(2,num):
        if num%i==0:
            y=False
    return y
ls1=eval(input())
ls2=[]
for i in range(len(ls1)):
    num=int(ls1[i])
    if sushu(num):
        ls2.append(ls1[i])
    else: pass
print(ls2)
