a=input()
print(a)
lst=a.split(" ")
n,m=int(lst[0]),int(lst[1])
if "-"in a:
    print("illegal input")
elif "."in a:
    print("illegal input")
elif m-n<=2:
    print("illegal input")
else:
    lst1=[x for x in range(n,m)]
    print(lst1)

