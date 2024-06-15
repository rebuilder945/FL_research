num=int(input())
a=1
b=2
ls1=[1,2]
ls2=[2,3]
d=0
for i in range (1,num+2):
    if i<=num:
        d+=b/a
        if a>1 and b>2:
            a=ls1[i-2]+ls1[i-1]
            ls1.append(a)
            b=ls2[i-2]+ls2[i-1]
            ls2.append(b)
        if a==1 and b==2:
            a=ls1[1]
            b=ls2[1]
    if i>num:
        print("%.4f"%d)
    
        



