a=input()
if len(a)==18:
    b=["7","9","10","5","8","4","2","1","6","3","7","9","10","5","8","4","2"]
    s=0
    for i in range(17):
        s+=(int(a[i]))*(int(b[i]))
    s=s%11
    ls1="0-1-2-3-4-5-6-7-8-9-10"
    ls1=ls1.split("-")
    ls1=[int(x) for x in ls1]
    ls2="1-0-X-9-8-7-6-5-4-3-2"
    ls2=ls2.split("-")
    m=ls1.index(s)
    n=ls2[m]
    if n==a[17]:
        print("Correct")
    else:
        print("Wrong")

else:
    print("error")
