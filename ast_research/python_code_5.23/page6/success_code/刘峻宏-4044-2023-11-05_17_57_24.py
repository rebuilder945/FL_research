from shlex import join


a=eval(input())
if a>=100:
    list=[]
    m=0
    for i in range(100,a):
        b=i//100
        c=(i-100*b)//10
        d=(i-100*b-10*c)
        if b**3+c**3+d**3==i:
            list.append(str(i))
            m=m+1
if m==0:
    print ("None")
else:
    print(" ".join(list))
