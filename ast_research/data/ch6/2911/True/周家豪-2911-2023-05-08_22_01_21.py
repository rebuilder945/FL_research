lst=list(map(int,input()))
for i in range(len(lst)):
    lst[i]=(lst[i]+5)%10
for i in range(len(lst)//2):
    lst[i],lst[-i-1]=lst[-i-1],lst[i]
print("".join (str(i) for i in lst))
