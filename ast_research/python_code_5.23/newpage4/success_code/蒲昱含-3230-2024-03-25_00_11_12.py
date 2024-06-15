mylist=[]
a=input()
mylist=(eval(a))
mylist.sort
b=0
for i in range(len(mylist)):
    c=mylist[i]
    b+=c*(10**i)
print(b)
