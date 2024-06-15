a=eval(input())
lst=[]
for i in range(100,a+1):
    i=str(i)
    if int(i[0])**3 + int(i[1])**3 + int(i[2])**3 == int(i):
        lst.append(i)
#if lst:
#    for i in lst:
#        print(i)
if len(lst)!=0:
    print(*lst,sep="\n")
else:
    print("none")
