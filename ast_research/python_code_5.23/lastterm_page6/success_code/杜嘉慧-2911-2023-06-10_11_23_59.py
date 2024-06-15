a=input()
lst=[]
for x in range(len(a)):
    lst.append(a[x])
for i in range(len(lst)):
    lst[i]=(lst[i]+5)%10
lst.sort(reverse=True)
for x in lst:
    print(x)
