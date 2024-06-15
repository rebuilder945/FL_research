
a=input()
b=list(a)
if len(b)==18:
    c=list(map(int,b[:17]))
    d=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum=0
    for i in range(0,17):
        sum+=c[i]*d[i]
    e=sum%11

    m=(12-e)%11
    if m==10:
        j='x'
    else:
        j=m

    
    if str(j)==a[-1]:
        print("Correct")
    else:
        print("Wrong")
else:
    print('Error')


