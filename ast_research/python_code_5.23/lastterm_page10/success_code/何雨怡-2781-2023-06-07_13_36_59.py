id=input()
idlist=list(id)
if 'X' in idlist:
    idlist.remove('X')
    idlist.append(10)
xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(idlist)!=18:
    print("Error")
else:
    sum=0
    for i in range(len(idlist)-1):
        plus=eval(idlist[i])*xishu[i]
        sum+=plus
    yushu=sum-(sum//11)*11
    yushulist=[0,1,2,3,4,5,6,7,8,9,10]
    reflect=[1,0,10,9,8,7,6,5,4,3,2]
    location=yushulist.index(yushu)
    final=reflect[location]
    if final==idlist[len(idlist)-1]:
        print('Correct')
    else:
        print("Error")
