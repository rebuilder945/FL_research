lst=list(map(int,input()))
lst1=[]
for i in lst :
    i=(i+5)%10
    lst1.append(i)
lst1[0],lst1[-1]=lst1[-1],lst1[0]
lst1[1],lst1[-2]=lst1[-2],lst1[1]
print(*lst1,sep="")
    
