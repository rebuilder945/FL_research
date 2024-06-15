list=eval(input())
list.reverse()
nlist=[]
for num in list:
    if num not in nlist:
        nlist.append(num)
nlist.reverse()
