mylist=[]
a=input()
mylist=(int(a))
for i in range(len(mylist)):
    if mylist[i]==0:
        del mylist[i]
        mylist.append(0)
        continue
    else:
        print(mylist)

