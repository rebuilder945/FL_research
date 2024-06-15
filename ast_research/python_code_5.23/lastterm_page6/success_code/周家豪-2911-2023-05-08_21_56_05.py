lst=list(map(int,input()))
for i in range(len(lst)):
    lst[i]=(lst[i]+5)%10
lst[0],lst[-1]=lst[-1],lst[0]
lst[1],lst[-2]=lst[-2],lst[1]
print("".join (str(i) for i in lst))
