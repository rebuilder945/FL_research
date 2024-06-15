lst=eval(input())
dict={}
for x in lst:
    for i in x:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
lst=list(dict.items())
lst1=sorted(lst,key=lambda x:(x[0]))
for i,j in lst1:
    print("%s,%d"%(i,j))
