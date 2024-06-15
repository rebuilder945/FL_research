from pickletools import read_unicodestring1


def sushu(x):
    lst1=list(range(2,x))
    jishu=0
    for x1 in lst1:
        if x%x1==0:
            jishu+=1
    if jishu==0:
        return 1
    else:
        return 0
def huiwen(x):
    b=str(x)
    lst1=list(b)
    lst2=lst1.copy()
    lst1.reverse()
    if lst1==lst2:
        return 1
    else:
        return 0

a=eval(input())
if type(a)!=int or a<=0:
    print("illegal input")
else:
    lst1=list(range(2,a+1))
    lst2=[]
    for x in lst1:
        if sushu(x)+huiwen(x)==2:
            lst2.append(x)
for i in lst2:
    print(i,end=' ')
    
           

