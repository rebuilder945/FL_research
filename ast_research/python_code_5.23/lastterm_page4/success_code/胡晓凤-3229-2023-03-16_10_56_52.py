lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
        lst1.sort()
        s=''
        for i in range(len(lst1)):
            s+=str(lst1[i])
            print(s)
    else:
        print("False")
