a=input()
lst=list(a)
lst1=[]
for i in lst:
    a=(int(i)+5)%10
    lst1.append(a)
for x in range(len(lst1)//2):
    lst1[x],lst1[-x-1]=lst1[-x-1],lst1[x]
for i in lst1:
    print(i,end='')
