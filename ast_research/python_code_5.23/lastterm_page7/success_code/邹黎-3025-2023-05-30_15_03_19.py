import copy
lst=list(input().split(" "))
lst0=[]
max=0
for x in lst:
    if lst.count(x)>=max:
        max=lst.count(x)
for x in lst:
    if  lst.count(x)==max and (x not in lst0):
        lst0.append(x)
lst0.sort()
for x in lst0:
    print(x+" "+str(max))
