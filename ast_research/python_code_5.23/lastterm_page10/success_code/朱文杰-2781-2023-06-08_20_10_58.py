x=input()
ls=[]
x=x.split()
xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
for i in range(len(x)-1):
    ls.append(x[i]*xishu[i])
    n=sum(ls)%11
    m=(12-n)%11
if x[17]=="X":
    x[17]="10"
if len(i)!=18:
    print("Error")
elif m==int(x[17]):
    print("Correct")
else:
    print("Wrong")
