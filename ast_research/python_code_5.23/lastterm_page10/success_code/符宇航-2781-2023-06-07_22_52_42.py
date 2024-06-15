number=list(input())
if len(number)!=18:
    print('Error')
else:
    xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    jieguo=[]
    for i in range(len(number)-1):
        n=int(number[i])*xishu[i]
        jieguo.append(n)
    a=sum(jieguo)%11
    xiaoyan=[1,0,'X',9,8,7,6,5,4,3,2]
    qq=xiaoyan[a]
    if qq==number[-1]:
        print('Correct')
    else:
        print('Wrong')

