string=input()
num=''
lst=[]
for x in range(len(string)):
    if string[x].isalpha():
        if string[x+1].isalpha():
            num+=string[x]
        else:
            lst.append(num)
            num=''
        lst.append(num)
if num==0:
    print('No digits')
else:
    if len(lst)==1:
        print(lst[0])
    else:
        lst1=[]
        for x in lst:
            n=len(x)
            lst1.append(n)
        for y in range(0,len(lst),-1):
            if len(lst[y])==max(lst1):
                print(lst[y])
                break

