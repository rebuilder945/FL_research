lst1=str(input())
for i in range(len(lst1)):
    lst1[i]=eval(lst1[i]+5)%10
lst1[0],lst1[-1],lst[1],lst1[-2]=lst1[-1],lst1[0],lst1[-2],lst1[1]
for i in lst1:
    print(1,"end=")
