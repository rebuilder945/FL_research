a=input()
lst=[]
for x in range(len(a)):
    lst.append(int(a[x]))
for i in range(len(lst)):
    lst[i]=(lst[i]+5)%10
lst.reverse()
for x in lst:
    print(x,end="")
