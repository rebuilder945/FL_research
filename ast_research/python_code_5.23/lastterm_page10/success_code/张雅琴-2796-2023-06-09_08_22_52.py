a=input()
num=0
for i in a:
    if i.isdigit():
        num+=1
if num==0:
    print("No digits")
else:
    b=len(a)
    lst=[]
    leng=0
    for i in range(0,b):
        for j in range(0,b-1):
            s=a[i:i+j+1]
            c=0
            for x in s:
                if x.isdigit():
                    c+=1
            if c==len(s) and len(s)>=leng:
                leng=len(s)
                lst.append(s)
    print(lst[-1])



