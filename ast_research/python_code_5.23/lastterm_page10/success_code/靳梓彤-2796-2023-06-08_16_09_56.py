string=input()
num=''
lst=[]
for x in string:
    if x.isdigit():
        num+=x
    else:
        lst.append(num)
        num=''
    lst.append(num)
if num=='':
    print("No digits")
else:
    if len(lst)==1:
        print(lst[0])
    else:
        lst1=[]
        for x in lst:
            n=len(x)
            lst1.append(n)
        for y in range(len(lst)-1,-1,-1):
            if len(lst[y])==max(lst1):
                print(lst[y])
                break

