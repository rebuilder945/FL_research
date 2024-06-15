lst=list(input())
for i in range(len(lst)):
    i=(i+5)%10
lst[0],lst[1],lst[-1],lst[-2]=lst[-1],lst[-2],lst[0],lst[1]
for i in lst:
    print(i,end="")
