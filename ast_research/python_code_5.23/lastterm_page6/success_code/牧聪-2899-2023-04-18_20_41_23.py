a=input()
lst=a.split(" ")
if "-"or"."in a:
    print("illegal input")
elif lst[1]-lst[0]<=2:
    print("illegal input")
else:
    lst1=[x for x in range(lst[0],lst[1]-1)]
    print(lst1)

