a=input()
if len(a)!=18:
    print("Error")
else:
    xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    n=0
    for i in range(16):
        n+=a[i]*xishu[i]
    n=n%11
    m=a[-1]
    if n==2 and m==X:
        print("Correct")
    elif m==(12-n)%11:
        print("Correct")
    else:
        print("Wrong")







