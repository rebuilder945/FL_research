lst=eval(input())
a="".join(lst)
lst1=[chr(ord('a')+i for i in range(26))]
lst2=[0]*26
for x in a:
    b=lst1.index(x)
    lst2[b]+=1
for i in range(len(lst2)):
    if lst2[i]!=0:
        print(lst1[i],lst2[i],sep=",")
