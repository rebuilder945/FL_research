string=input()
num=''
lst=[]
n=0
for x in string:
    if x.isdigit():
        num+=x
        n+=1
    else:
        lst.append(num)
        num=''
    lst.append(num)
if n==0:
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

