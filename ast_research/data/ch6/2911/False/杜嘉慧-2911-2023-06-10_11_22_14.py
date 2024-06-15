lst=input.split("")
for i in range(len(lst)):
    lst[i]=(lst[i]+5)%10
lst.sort(reverse=True)
for x in lst:
    print(x)
