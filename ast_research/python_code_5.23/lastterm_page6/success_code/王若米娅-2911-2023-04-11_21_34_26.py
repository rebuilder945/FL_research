str=input()
lst=list(int(i) for i in str.split())
lst1=[]
for x in lst:
    c=(x+5)%10
    lst1.append(c)
lst1[-1]=lst1[0]
lst1[-2]=lst1[1]
print(*lst1,sep='')
