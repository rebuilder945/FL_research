def identify(x):
    ls=[]
    xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for i in range(len(x)-1):
        ls.append(int(x[i])*xishu[i])
        n=sum(ls)%11
        return (12-n)%11
i=input()
if i[17]=="X":
    i[17]="10"
if len(i)!=18:
    print("Error")
elif identify(i)==int(i[17]):
    print("Correct")
else:
    print("Wrong")
