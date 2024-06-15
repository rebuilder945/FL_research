a=input()
lst=[]
c=0
if a==" ":
    print("None")
else:
    for x in range(0,len(a)):
        lst.append([a.count(a[x]),x])
    for x in range(0,len(lst)):
        if lst[x][0]==1:
            print(a[x])
            break
        else:
            c+=1
        if c==len(lst):
            print("None")

