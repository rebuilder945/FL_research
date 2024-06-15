n=input()
if len(n)!=18:
    print("Error")
else:
    lst=[int(x) for x in n[0:17]]
    lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    s=0
    for i in range(17):
        s=s+lst[i]*lst1[i]
    s1=s%11
    s2=(12-s1)%11
    s3="X" if s2==10 else str(s2)
    if s3==n[-1]:
        print("Correct")
    else:
        print("Wrong")

