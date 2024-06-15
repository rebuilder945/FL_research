n=input()
lst={}
while n!="q":
    if n not in lst:
        lst[n]=1
    else:
        lst[n]+=1
    n=input()
lst2=sorted(list(lst.items()),key=lambda x:x[1],reverse=True)
print("%s %d"%(lst2[0][0],lst2[0][1]))


