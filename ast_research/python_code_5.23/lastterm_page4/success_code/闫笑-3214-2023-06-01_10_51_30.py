lst = eval(input())
a =0
for x in range(0,len(lst)+1):
    if lst[x]!=0:
        lst[a],lst[x]=lst[x],lst[a]
    else:
        a+=1
print(lst)


    

